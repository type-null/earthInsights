import numpy as np
import pandas as pd

# filename = "StudentForm (Combined) (Responses).xlsx"

sc = ['c1','c3','c5','c6']
course = ['c1','c2','c3','c4','c5','c6','c7','c8']

def preprocess(filename):
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

def get_pref(df, sc=False):
    '''
    Returns a dictionary of students' preferences, with student UNI as the key
    sc=False gives all courses, sc=True gives only semi-core courses
    '''
    pref_dict = {}
    if sc:
        for UNI, row in df.loc[:,'R1':'R8'].iterrows():
            sc_list = []
            for c in row.values:
                if c in ['c1','c3','c5','c6']: # if course is semi-core
                    sc_list.append(c)
            pref_dict[UNI] = sc_list

    else:  
        for UNI, row in df.loc[:,'R1':'R8'].iterrows():
            pref_dict[UNI] = list(row.values)

    return pref_dict








