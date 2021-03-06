import numpy as np
import pandas as pd
from collections import Counter


sc = ['c1','c3','c5','c6']
course = ['c1','c2','c3','c4','c5','c6','c7','c8']
hd = ['c1','c2','c3','c4']
ld = ['c5','c6','c7','c8']
# time conflit course pair
coursePair = [{'c1', 'c4'}, {'c2', 'c8'}, {'c3', 'c5'}, {'c6', 'c7'}]


class Assign:
    def __init(self):
        pass
    
    
    def preprocess(self, filename):
        """
        Separate file to two groups
        """
        df = pd.read_excel(filename, header=None)
        df= df.replace(to_replace = {'Business Analytics':'c1', 
                                 'Cloud Computing' : 'c2',
                                 'Machine Learning' : 'c3',
                                 'Data Analytics': 'c4',
                                 'Optimization': 'c5',
                                 'Stochastic': 'c6',
                                 'Simulation': 'c7',
                                 'Computational Discrete Optimization': 'c8'
                                 },
                   value = None)

        # extract group 1 and group 2 data from combined df
        df_group1 = df[df.iloc[:,3]=="Even (0, 2, 4, 6, 8)"].drop(columns=range(20,40)).replace(to_replace={'Even (0, 2, 4, 6, 8)':'Group1'})
        df_group2 = df[df.iloc[:,3]=="Odd (1, 3, 5, 7, 9)"].drop(columns=range(4,20)).replace(to_replace={'Odd (1, 3, 5, 7, 9)':'Group2'})

        # set colnames
        df_group1_colnames = ['Timestamp','Student','Gender','Group',
                              'c1','c2','c3','c4','c5','c6','c7','c8', # bids on courses
                              'R1','R2','R3','R4','R5','R6','R7','R8'  # ranks
                              ]
        df_group2_colnames = ['Timestamp','Student','Gender','Group',
                              'R1','R2','R3','R4','R5','R6','R7','R8', # ranks
                              'c1','c2','c3','c4','c5','c6','c7','c8', # bids on courses
                              't1','t2','t3','t4'                      # bids on time slots
                              ]

        df_group1.columns = df_group1_colnames
        df_group2.columns = df_group2_colnames

        # change datatype of bids from str to int
        df_group1 = df_group1.apply(pd.to_numeric, downcast='integer', errors='ignore')
        df_group2 = df_group2.apply(pd.to_numeric, downcast='integer', errors='ignore')

        # index each student using their UNI
        df_group1.index = df_group1.Student.str[:6]
        df_group1.index.name = 'UNI'
        df_group2.index = df_group2.Student.str[:6]
        df_group2.index.name = 'UNI'

        # check bid criteria is met
        df_group1['CourseBidCriteria'] = (df_group1.loc[:,'c1':'c8'].sum(axis=1) == 100)
        df_group2['CourseBidCriteria'] = (df_group2.loc[:,'c1':'c8'].sum(axis=1) == 100)
        df_group2['TimeBidCriteria'] = (df_group2.loc[:,'t1':'t4'].sum(axis=1) == 100)

        return df_group1, df_group2

    
    def get_pref(self, df, sc=False):
        '''
        Returns a dictionary of students' preferences, with student UNI as the key
        sc=False gives all courses, sc=True gives only semi-core courses
        '''
        pref_dict = {}
        if sc:
            for UNI, row in df.loc[:, 'R1':'R8'].iterrows():
                sc_list = []
                for c in row.values:
                    if c in ['c1','c3','c5','c6']: # if course is semi-core
                        sc_list.append(c)
                pref_dict[UNI] = sc_list

        else:  
            for UNI, row in df.loc[:,'R1':'R8'].iterrows():
                pref_dict[UNI] = list(row.values)

        return pref_dict
        
    
    def get_bid_pref(self, df, sc=False):
        '''
        Returns a dictionary of students' preferences, derived from course bids.
        Student UNI as key.
        sc=False gives all courses, sc=True gives only semi-core courses
        '''
        pref_dict = {}
        if sc:
            for UNI, row in df.loc[:,'c1':'c8'].iterrows():
                sc_list = []
                for c in row.sort_values(ascending=False).index.values:
                    if c in ['c1','c3','c5','c6']: # if course is semi-core
                        sc_list.append(c)
                pref_dict[UNI] = sc_list

        else:
            for UNI, row in df.loc[:,'c1':'c8'].iterrows():
                pref_dict[UNI] = list(row.sort_values(ascending=False).index.values)
      
        return pref_dict


    def modified_bid(self, df, seed=42):
        '''
        Adds a random real number x drawn from uniform distribution for each student-course pair
        Modifies each positive bid b>0 as b'=b+x
        Returns a modified bid matrix
        '''
        np.random.seed(seed)
        df_ = df.loc[:,'c1':'c8']
        X = np.random.uniform(size=df_.shape)
        mod_bids = df_ + X
        # mod_bids[mod_bids < 1] = 0
        return mod_bids


    def lottery(self, ds, seed=42, reverse=False):
        '''
        Uses a unique lottery to create a fake bid df for matching
        '''
        np.random.seed(seed)
        ds = ds.reset_index()
        if reverse:
            list_ = np.flip(np.random.permutation(ds['UNI']))
        else:
            list_ = np.random.permutation(ds['UNI'])
        lotteryBids = pd.DataFrame([([u]+[100-r]*8) for r,u in enumerate(list_)]).set_index(0)
        lotteryBids.columns = course
        return lotteryBids


    def timeToCourse(self, df):
        """
        Converts time bids to course bids
        """
        # check that the dataframe passed into function contains time bids
        try:
            df.loc[:,'t1':'t4']
        except:
            print("No timeslot keys found. This function only works for df_group2.")

        new_df = df.loc[:,'R1':'R8']
        new_df['c1'] = df.t2; new_df['c2'] = df.t3; new_df['c3'] = df.t4; new_df['c4'] = df.t2
        new_df['c5'] = df.t4; new_df['c6'] = df.t1; new_df['c7'] = df.t1; new_df['c8'] = df.t3
        return new_df    

    
    def capacity(self, df, same=False, buffer=3):
        """
        Generate course capacities
        """
        cap = {c: 0 for c in course}

        if not same:
            # 4 semi-core courses take at least len(df) people
            capOfSC = round(len(df)/4)
            lastSC = len(df) - 3*capOfSC
            for c in sc:
                cap[c] += capOfSC
            cap[sc[0]] = lastSC

            remainTotalSeats = 3*len(df) - 3*capOfSC - lastSC
            capOfAll = round(remainTotalSeats/8)
            for c in course:
                cap[c] += capOfAll

            ldCap = {c: len(df) for c in ld}
            cap.update(ldCap)

        if same:
            # as per Yuri's recc, give all classes same capacity
            # allCap = minimum capacity per class + some buffer
            allCap = round(3*len(df)/8) + buffer
            cap = {c: allCap for c in course} 

        return cap


    def newCap(self, c, k, bid_sc_k):
        """
        Calculate new capacity by minus seats already got
        """
        a = 0
        if bid_sc_k.get(c):
            a = len(bid_sc_k.get(c))
        return k - a
    
    ### Assign Algorithm
    
    def assignSC(self, df, bidPref=False, test4=False):
        """
        Assign 1 semi-core
        """
        stop = False
        r = 0                                   # starts with 0 (first round)
        cap = self.capacity(df)                 # init capacity
        if bidPref:
            pref_sc = self.get_bid_pref(df, sc=True) # get implied pref list of sc from bids
        else:
            pref_sc = self.get_pref(df, sc=True)     # get pref list of sc
        pref_sc_z = {}                          # pref to be updated each round
        rejected = pref_sc.keys()
        # print(pref_sc)

        while not stop:
            # get first(round#) sc course on each one's pref list
            pref_sc_r = {u: x[r] for (u,x) in pref_sc.items() if u in rejected}
            # modify pref list
            pref_sc_z.update(pref_sc_r)   # here because later updating bid list would be the same

            # rank students for each sc by bidding
            if not test4:
                bid_sc = {c: sorted([((self.modified_bid(df)).loc[u,c], u) 
                              for u in pref_sc_z.keys() 
                              if pref_sc_z[u] == c], reverse=True) 
                          for c in sc}

            elif test4:
                bid_sc = {c: sorted([((self.lottery(df)).loc[u,c], u) 
                              for u in pref_sc_z.keys() 
                              if pref_sc_z[u] == c], reverse=True) 
                           for c in sc}

            # keep top k students
            bid_sc_k = {c: s[:cap[c]] for (c, s) in bid_sc.items()}
            print(bid_sc_k)

            # find the list of unmatched student unis
            rejected = [i[1] for l in [s[cap[c]:] for (c, s) in bid_sc.items()] for i in l]

            if rejected: # not empty
                r += 1
            else:
                stop = True

        # update capacity
        cap = {c: self.newCap(c, k, bid_sc_k) for (c, k) in cap.items()}

        print("Part I (Semi-core): Number of GS rounds:",r+1)
        # print(bid_sc_k)
        return bid_sc_k, cap
    
    
    def courseToStudentView(self, courseView):
        """
        Convert {course: [(bid, uni)]} to {uni: [courses]}
        """
        courseViewUni = {c: [s[1] for s in courseView[c]] for c in courseView.keys()}
        studenView = {u: [] for l in courseViewUni.values() for u in l}
        for c in courseViewUni.keys():
            for u in courseViewUni[c]:
                studenView[u].append(c)
        return studenView

    
    def resolveTimeConflict(self, df, courseView, bidPref=False):
        """ 
        Update preference list by deleting conflict courses
        """
        if bidPref:
            updatedPref = self.get_bid_pref(df)
        else:
            updatedPref = self.get_pref(df)
        studentView = self.courseToStudentView(courseView)
        for u in studentView.keys():
            assignedSC = studentView[u][0]
            for pair in coursePair:
                if assignedSC in pair:
                    updatedPref[u] = [i for i in updatedPref[u] if i not in pair]

        return updatedPref

    
    def assign(self, df, pref, cap, courseNum=2, test4=False):
        """
        General assignment (2 courses default)
        """
        stop = False
        r = 0                                                # round, not used in this function
        rejected = pref.keys()
        nextProposeQuota = {u: courseNum for u in rejected}  # # of courses rejected last turn
        propose = {u: [] for u in pref.keys()}               # store courses to be proposed in each turn
        proposed = propose                                   # store proposed courses

        while not stop:
            # first propose to 2 courses, then propose to quota courses
            newPropose = {u: [c for c in x if c not in proposed[u]][:nextProposeQuota[u]]
                              for (u,x) in pref.items() if u in set(rejected)}
            # update propose and proposed
            for u in newPropose.keys():
                propose[u].extend(newPropose[u])
                proposed[u].extend(newPropose[u])
            # print(propose)  # uncomment this to see glitch

            # index bids
            if not test4:
                bid1 = {c: [((self.modified_bid(df)).loc[u,c], u) for u in propose.keys() if propose[u][0] == c] 
                       for c in course}
                bid2 = {c: [((self.modified_bid(df)).loc[u,c], u) for u in propose.keys() if propose[u][1] == c]
                       for c in course}
            elif test4:
                bid1 = {c: [((self.lottery(df)).loc[u,c], u) for u in propose.keys() if propose[u][0] == c] 
                        for c in course}
                bid2 = {c: [((self.lottery(df)).loc[u,c], u) for u in propose.keys() if propose[u][1] == c]
                        for c in course}
            bid = {c: sorted(l + bid2[c], reverse=True) for (c,l) in bid1.items()}

            # keep top k students
            bid_k = {c: s[:cap[c]] for (c, s) in bid.items()}

            # find the list of unmatched student unis
            rejected = [i[1] for l in [s[cap[c]:] for (c, s) in bid.items()] for i in l]

            # record current proposal
            propose = {u: [] for u in pref.keys()}
            propose.update(self.courseToStudentView(bid_k))

            # if no one get rejected, check time conflict
            if all([len(cl)==2 for cl in propose.values()]):
                # reject second course (less preferred) due to time conflict
                rejected = [u for u in propose.keys() if set(propose[u]) in coursePair]
                # update propose
                for u in rejected:
                    propose[u].pop()

            if rejected: # not empty
                r += 1
                nextProposeQuota = Counter(rejected)
            else:
                stop = True

        print("Part II (General)  : Number of GS rounds:",r+1)
        # print(bid_k)
        return bid_k
    
    
    def test(self, filename, test=1, group=1):
        """
        test=1: bid
        test=2: bid + preference
        test=3: preference + time slot
        test=4: time order
        """
        (df_group1, df_group2) = self.preprocess(filename)
        if group == 1:
            df = df_group1
        elif group == 2:
            df = df_group2
        else:
            print("Group index out of range!")

        bidPref = False
        test4 = False

        if test == 1:
            bidPref = True
        elif test == 2:
            pass
        elif test == 3:
            if group == 2:
                df = self.timeToCourse(df)
            else:
                print("Test 3 only applies to df_group2.")
        elif test == 4:
            test4 = True
        else:
            print("Test # out of range!")

        print(f"Assigning according test {test} with group {group} ...")
        (courseViewSC, cap) = self.assignSC(df, bidPref=bidPref, test4=test4)
        updatedPref = self.resolveTimeConflict(df, courseViewSC, bidPref=bidPref)
        courseView = self.assign(df, updatedPref, cap, test4=test4)
        
        # convert to {uni: course-list}
        studentViewSC = self.courseToStudentView(courseViewSC)
        studentView = self.courseToStudentView(courseView)
        # return studentView
        
        # combine sc with other courses
        for u in studentView.keys():
            studentView[u].extend(studentViewSC[u])
            
        # The last (third) course is the semi-core requirement
        return studentView


    def reportRank(self, studentView):
        """
        Compute average rank
        """
        trueRank = {u: {c: i for i, c in enumerate(prefs)} 
                        for u, prefs in self.get_pref(df).items()}
        studentAvgRank = {u: round(sum([trueRank.get(u).get(c) 
            for c in m])/3,3) for u, m in studentView.items()}
        testAvgRank = round(sum([r for (u,r) in studentAvgRank.items()])/len(trueRank),4)
        
        print('Test Average Rank:', testAvgRank)
        return testAvgRank, studentAvgRank




