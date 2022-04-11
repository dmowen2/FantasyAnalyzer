import pandas

from fantasyanalyzer.pulldata import queries, plotting
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


abrvQuery = queries.query("C:\\Users\\bluem\\vscodeprojects\FantasyAnalyzer\sheets\\teaminfo.csv")
years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
rankanddifferences = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [],
                      8: [], 9: [], 10: [], 11: [], 12: [], 13: [], 14: [], 15: [], 16: [],
                      17: [], 18: [], 19: [], 20: [], 21: [], 22: [], 23: [], 24: [], 25: [],
                      26: [], 27: [], 28: [], 29: [], 30: [], 31: [], 32:[]}

for year in years:

    gamebygameQuery = queries.query(
    "C:\\Users\\bluem\\vscodeprojects\FantasyAnalyzer\seasonalgame\\fantasy" + str(year) + ".csv")

    gamebygameQuery.queryPos("RB", True)

    defenserankingQuery = queries.query("C:\\Users\\bluem\\vscodeprojects\FantasyAnalyzer\seasonaldefense\\"+ str(year) + "def.csv")


    hold = gamebygameQuery.getQuery().groupby('Name').agg({'FantPt': ['mean']})
    ppgdf = hold



    for index, row in gamebygameQuery.getQuery().iterrows():

        name = row['Name']
        findnamerow = ppgdf.loc[[name]]
        playermean = findnamerow[('FantPt', 'mean')][name]
        opp = row['Opp']

    # get team name index from the abbreviation

        if opp == 'OAK':
            opp = 'LVR'
        elif opp == 'STL':
            opp = 'LAR'
        elif opp == 'SDG':
            opp = 'LAC'
        getnameindex = abrvQuery.getQuery().index[abrvQuery.getQuery()['Abbreviation'] == opp].tolist()
    # find team name from team info
        teamname = abrvQuery.getQuery().at[getnameindex[0], 'Name']

    # find the index of the defense
        defrankindex = defenserankingQuery.getQuery().index[defenserankingQuery.getQuery()['Tm'] == teamname].tolist()

    # This gets the defensive rank according to the matchup Rank.2 is rushing (its screwed up i know but tbh changing
    # it is not worth the time)


        if defrankindex == []:
            defrankindex = defenserankingQuery.getQuery().index[defenserankingQuery.getQuery()['Tm'] == "Washington Redskins"].tolist()
        defrank = defenserankingQuery.getQuery().at[defrankindex[0], 'Rank.2']

        # Rank.1 = receiving yard points allowed ranking Rank.2
        difference = (playermean-row['FantPt'])*-1
        if (str(difference) != 'nan'):
            rankanddifferences[int(float(defrank))] += [(playermean-row['FantPt'])*-1]



    # simply print the differences
    #  print(str(opp) + ": " + str((playermean-row['FantPt'])*-1))

    # find the ranking for the defense for rushing sinces its running back

# print(rankanddifferences[16])
# print(ppgdf)

    breakdown = list(rankanddifferences.items())
    stattuplelist = []

# have to zip each key with all the values in the associated list for easier plotting
avgs = []
for k in rankanddifferences.keys():
    div = len(rankanddifferences[k])
    if (div == 0):
        div = 1

    avgs += [sum(rankanddifferences[k])/div]

for (k, v) in breakdown:
    stattuplelist += map(lambda e: (k, e), v)

fig, ax = plt.subplots()
x_values = [x[0] for x in stattuplelist]
y_values = [y[1] for y in stattuplelist]
# ax.scatter(x_values, y_values, label="")
ax.plot(rankanddifferences.keys(), avgs, color='Red', label='Averages')
print(avgs)
plt.title("RB Avg Difference in score vs Defensive Fantasy points allowed ranking")
plt.legend()
plt.show()
