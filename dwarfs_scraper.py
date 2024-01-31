from bs4 import BeautifulSoup
import pandas as pd
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(START_URL)
soup = BeautifulSoup(page.content, "html.parser")

dwarf_star_data = []

dwarf_table = soup.find_all("table", attrs={"class", "wikitable"})
table = dwarf_table[1].find_all('tr')

temp_list= []

for tr in table:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

stars_data  = []

for i in range(0, len(dwarf_star_data)):
    Star_names = dwarf_star_data[i][1]
    Radius = dwarf_star_data[i][6]
    Mass = dwarf_star_data[i][5]
    Distance = dwarf_star_data[i][3]
    required_data = ["Star name","radius", "mass", "distance data"]
    stars_data.append(required_data)

print(stars_data)

headers = ["Star name","radius", "mass", "distance data"]
dwarf_star  = pd.DataFrame(dwarf_star_data, columns = headers)
dwarf_star.to_csv('dwarf_star_data.csv', index=True, index_label="id")