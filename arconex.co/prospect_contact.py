
import re
import bs4
import requests
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile


# read excel
df = pd.read_excel('~/Downloads/sample - arch prospecting.xlsx', sheet_name='sample arch list')

# read architect in row i
i = 1
license = df['License #'][i]
business = df['Business Name'][i]
firstName = df['First Name'][i]
lastName = df['Last Name'][i]

query = "%20".join([firstName, lastName, "architect"])
searchURL = f'https://www.google.com/search?pz=1&cf=all&ned=us&hl=en&tbm=nws&gl=us&as_q={query}'

userAgent = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0"
response = requests.get(searchURL, headers={'User-Agent': userAgent})
if response.status_code == 200:
    print("Searching ...")
    # print(response.content.decode('utf-8'))
else:
    print(f"Fail to get the url [{response.status_code}]")

# parsing
soup = bs4.BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
# snippet = [a.text for a in soup.find_all('div', class_="Y3v8qd")]
links = [a['href'] for a in soup.find_all('a', href=True)]
# clean links
pattern = r'^https://\w+\.(?!google).\S+'
newsLinks = [re.findall(pattern, a)[0] for a in links if re.findall(pattern, a)]