import pandas as pd
from bs4 import BeautifulSoup
import requests


# setup functions to initially pull the data off of the website and get the initial cv files
class setup:

    # pulls all players fantasy football data based off the year
    def runPullPlayerData(self, year):
        url = 'https://www.pro-football-reference.com'
        year = year
        maxp = 300

        # grab fantasy players
        r = requests.get(url + '/years/' + year + '/fantasy.htm')
        soup = BeautifulSoup(r.content, 'html.parser')
        parsed_table = soup.find_all('table')[0]

        df = []

        # this pulls basically all the players

        # first 2 rows are col headers
        for i, row in enumerate(parsed_table.find_all('tr')[2:]):
            if i % 10 == 0: print(i, end=' ')
            if i >= maxp:
                print('\nComplete.')
                break

            try:
                dat = row.find('td', attrs={'sheets-stat': 'player'})
                name = dat.a.get_text()
                stub = dat.a.get('href')
                stub = stub[:-4] + '/fantasy/' + str(year)
                pos = row.find('td', attrs={'sheets-stat': 'fantasy_pos'}).get_text()

                # grab this players stats
                tdf = pd.read_html(url + stub)[0]
                # this was throwing an lxml error needed to install the respective package

                # get rid of MultiIndex, just keep last row
                tdf.columns = tdf.columns.get_level_values(-1)

                # fix the away/home column
                tdf = tdf.rename(columns={'Unnamed: 4_level_2': 'Away'})
                tdf['Away'] = [1 if r == '@' else 0 for r in tdf['Away']]
                # drop all intermediate stats
                tdf = tdf.iloc[:, [1, 2, 3, 4, 5, -3]]

                # drop "Total" row
                tdf = tdf.query('Date != "Total"')

                # add other info
                tdf['Name'] = name
                tdf['Position'] = pos
                tdf['Season'] = year

                df.append(tdf)
            except Exception as e:
                print(e)
                pass

        df = pd.concat(df)
        df.head()
        df.to_csv("..\..\\sheets\\fantasy2021.csv")
