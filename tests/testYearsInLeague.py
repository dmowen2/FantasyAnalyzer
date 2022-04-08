# https://www.pro-football-reference.com/players/A/AndrMa00.htm
# reference for the individual player


# need to look at my previously coded examples from cooper kupp and add those to the github

import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

ckuppurl = 'https://www.pro-football-reference.com/players/K/KuppCo00.htm'

#stores it as a pandas dataframe
ckuppdf = pd.read_html(ckuppurl)[0]



path = "C:\\Users\\bluem\\vscodeprojects\FantasyAnalyzer\sheets\\Kuppbasic.csv"

ckuppdf.columns = ckuppdf.columns.get_level_values(-1)


ckuppdf.to_csv(path)


print(ckuppdf['Year'])
print("Kupp years in league: " + str(len(ckuppdf['Year'])-2))


