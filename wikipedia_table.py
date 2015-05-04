#/usr/bin/env python
from bs4 import BeautifulSoup
import requests

url = 'http://en.wikipedia.org/wiki/List_of_ongoing_armed_conflicts'
columns = ['conflict', 'location']

headers = {'User-Agent': 'Mozilla/5.0'}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text)

tables = soup.findAll("table", { "class" : "wikitable sortable" })

row_count = 0
for table in tables:

    heading_indices = []
    temp =[]
    header = table.findAll("th")
    for heading in header:
        temp.append(heading.find(text=True).lower())
    for col in columns:
        i = temp.index(col.lower())
        heading_indices.append(i)

    results = []
    for i,row in enumerate(table.findAll("tr")):
        if i == 0:
            continue

        cells = row.findAll("td")
        for j in heading_indices:
            print cells[j].find(text=True)

        #print cells
        #print len(cells)
        

#print tables
#print len(tables)