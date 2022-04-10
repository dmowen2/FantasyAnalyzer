import pandas as pd
from bs4 import BeautifulSoup
import requests

url = 'https://www.pro-football-reference.com'
maxp = 300

# grab fantasy players


year = 2021
df = []

# first 2 rows are col headers

r = requests.get(url + '/years/' + str(year) + '/fantasy.htm')
soup = BeautifulSoup(r.content, 'html.parser')
parsed_table = soup.find_all('table')[0]

for i, row in enumerate(parsed_table.find_all('tr')[2:]):
        # if i == 1: break
        if i % 10 == 0: print(i, end=' ')

        if i >= maxp:
            print('\nComplete.')
            break

        try:
            dat = row.find('td', attrs={'data-stat': 'player'})
            name = dat.a.get_text()
            stub = dat.a.get('href')
            stub = stub[:-4] + '/fantasy/'
            pos = row.find('td', attrs={'data-stat': 'fantasy_pos'}).get_text()


            tdf = pd.read_html(url + stub)[0]
            tdf.columns = tdf.columns.get_level_values(-1)

            count = 0

            #calculate the number of years in the league for the player
            tdf = tdf.rename(columns={'Unnamed: 0_level_2': 'Year'})
            tdf['Name'] = name
            tdf['AvgFantPt'] = tdf['FantPt']/tdf['G']
            tdf['Position'] = pos

            holdlist = []
            j = 0;
            while j < len(tdf['Name']):
                holdlist.append(j)
                j += 1
            tdf['YINL'] = holdlist

            df.append(tdf[['Name', 'Position', 'Year', 'G', 'FantPt', 'AvgFantPt', "YINL"]].iloc[:-1, :])

        except Exception as e:
            pass

df = pd.concat(df)
df.head()
df.to_csv("C:\\Users\\bluem\\vscodeprojects\FantasyAnalyzer\seasonalsheets\\"+str(year)+"seasonalfantasydata.csv")

