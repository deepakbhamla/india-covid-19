import requests
import bs4
import tabulate
import os


extract_content = lambda row : [x.text.replace('\n','') for x in row]
URL = 'https://www.mohfw.gov.in/'
HEADINGS = ['SNO', 'State','Indian-Confirmed','Foreign-confirmed','Cured','Death']
response = requests.get(URL).content
soup  = bs4.BeautifulSoup(response,'html.parser')
header = extract_content(soup.tr.find_all('th'))
stats = []
all_rows = soup.find_all('tr')
for row in all_rows:
    stat = extract_content(row.find_all('td'))
    if stat:
        if len(stat) == 5:
            stat = ['',*stat]
            stat.append(stat)
        elif len(stat) == 6:
            stats.append(stat)

stats[-1][1] = "Total Cases"
stats.remove(stats[-1])

print(stats)