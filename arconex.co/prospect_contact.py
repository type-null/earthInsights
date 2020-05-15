"""
Scrape architect info for Arconex.co

"""

import re
import bs4
import requests
import pandas as pd


def readURL(url):
    """
    Return html if url is readable

    """
    userAgent = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0"
    response = requests.get(url, headers={'User-Agent': userAgent})
    if response.status_code == 200:
        return response.content.decode('utf-8')
    else:
        print(f"Fail to get the url [{response.status_code}]")
        return False


def googleNews(firstName, LastName):
    """
    Google News search for the architect’s name

    """
    print("Searching this person on Google News ...")
    source = {}
    query = "%20".join([firstName, lastName, "architect"])
    searchURL = f'https://www.google.com/search?pz=1&cf=all&ned=us&hl=en&tbm=nws&gl=us&as_q={query}'

    response = readURL(searchURL)
    if response:
        soup = bs4.BeautifulSoup(response, 'html.parser')
    else:
        print("Google search failed.")
    # snippet = [a.text for a in soup.find_all('div', class_="Y3v8qd")]
    links = [a['href'] for a in soup.find_all('a', href=True)]
    # clean links
    pattern = r'^https://\w+\.(?!google).\S+'
    newsLinks = [re.findall(pattern, a)[0] for a in links if re.findall(pattern, a)]

    for i in range(len(newsLinks)):
        newsURL = newsLinks[i]
        news = readURL(newsURL)

        if re.search(" ".join((firstName, lastName)), news, re.IGNORECASE):
            soup = bs4.BeautifulSoup(news, 'html.parser')
            source["title"] = soup.find_all('title')[0].text.strip()
            # source["date"] = soup.find_all('date')[0].text.strip()
            source["url"] = newsURL
            return source

    print("No match found in Google News.")
    return source


def yimby(firstName, LastName):
    """
    Search architects name on https://newyorkyimby.com/

    """
    print("Searching this person on YIMBY ...")
    source = {}
    url = f"https://newyorkyimby.com/?s={firstName}+{lastName}&orderby=post_date&order=desc"
    soup = bs4.BeautifulSoup(readURL(url), 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True, class_='button-excerpt-more button')]
    pattern = r'^https://newyorkyimby.com/[\d]+/[\d]+/\S+'
    newsLinks = [re.findall(pattern, a)[0].strip() for a in links if re.findall(pattern, a)]
    newsLinks = list(set(newsLinks))
    newsLinks = sorted(newsLinks, reverse=True)

    for i in range(len(newsLinks)):
        newsURL = newsLinks[i]
        news = readURL(newsURL)

        if re.search(" ".join((firstName, lastName)), news, re.IGNORECASE):
            soup = bs4.BeautifulSoup(news, 'html.parser')
            source["title"] = soup.find_all('title')[0].text.strip()
            source["url"] = newsURL
            return source

    print("No match found in YIMBY.")
    return source


def dob(licenseNo):
    """
    see if there are any large projects recently approved at the DOB

    """
    url = f'http://a810-bisweb.nyc.gov/bisweb/JobsByLicenseNumberServlet?alljappproftitle=RA&all'\
        'japplicnumber={licenseNo}&go20=+GO+&requestid=0&allinquirytype=BXS1LI08'

# read excel
df = pd.read_excel('~/Downloads/sample - arch prospecting.xlsx', sheet_name='sample arch list')
df = df.dropna().reset_index()

for i in range(len(df)):
    licenseNo = df['License #'][i]
    business = df['Business Name'][i]
    firstName = df['First Name'][i]
    lastName = df['Last Name'][i]
    print(f"=====----- {(i+1)/(len(df)+1)*100} % -----=====")
    print(f"Start collecting {firstName} {lastName}")

    gsource = googleNews(firstName, lastName)
    if gsource:
        df['Source ref'][i] = gsource["url"]
        df['XXXprojectXXX'][i] = gsource["title"]
        print("Got the info from Google News!")
        continue

    ysource = yimby(firstName, lastName)
    if ysource:
        df['Source ref'][i] = ysource["url"]
        df['XXXprojectXXX'][i] = ysource["title"]
        print("Got the info from YIMBY!")
        continue

    # dsource = dob(licenseNo)
    # if ysource:
    #     df['Source ref'] = dsource["url"]
    #     df['XXXprojectXXX'] = dsource["title"]

    continue

print(f"=====----- 100 % -----=====")
print("Seaching complete!")