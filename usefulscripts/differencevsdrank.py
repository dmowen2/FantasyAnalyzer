import numpy
import pandas

from fantasyanalyzer.pulldata import queries, plotting
import matplotlib.pyplot as plt
from sklearn.linear_model  import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import IsolationForest
import pandas as pd
import numpy as np


abrvQuery = queries.query("C:\\Users\\bluem\\vscodeprojects\FantasyAnalyzer\sheets\\teaminfo.csv")
years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
rankanddifferences = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [],
                      8: [], 9: [], 10: [], 11: [], 12: [], 13: [], 14: [], 15: [], 16: [],
                      17: [], 18: [], 19: [], 20: [], 21: [], 22: [], 23: [], 24: [], 25: [],
                      26: [], 27: [], 28: [], 29: [], 30: [], 31: [], 32:[]}
separateyear = 2021
singleyear = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [],
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


        if (year == separateyear):
            if (str(difference) != 'nan'):
                singleyear[int(float(defrank))] += [(playermean-row['FantPt'])*-1]

    # simply print the differences
    #  print(str(opp) + ": " + str((playermean-row['FantPt'])*-1))

    # find the ranking for the defense for rushing sinces its running back


# breaks down the dictionary into a list of tuples for easier handling
breakdown = list(rankanddifferences.items())
stattuplelist = []

# have to zip each key with all the values in the associated list for easier plotting
avgs = []

# Find the average for each individual rank
for k in rankanddifferences.keys():
    div = len(rankanddifferences[k])
    if (div == 0):
        div = 1
    avgs += [sum(rankanddifferences[k])/div]

# zip each key with all the values in the associated list for easier plotting
for (k, v) in breakdown:
    stattuplelist += map(lambda e: (k, e), v)


# Begin plotting
fig, ax = plt.subplots()



# further breaks down the values for plotting by getting each individual x value and corresponding y value
x_values = [x[0] for x in stattuplelist]
y_values = [y[1] for y in stattuplelist]

# single year breakdown
oneyearbreakdown = list(singleyear.items())
oneyearstattuplelist = []
for (k, v) in oneyearbreakdown:
    oneyearstattuplelist += map(lambda e: (k, e), v)

yearx_values = [x[0] for x in oneyearstattuplelist]
yeary_values = [y[1] for y in oneyearstattuplelist]

# necessary numpy array conversions for the linear model
xarr = numpy.array(x_values)
yarr = numpy.array(y_values)


x_train, x_test, y_train, y_test = train_test_split(xarr, yarr, test_size=.2)

# plt.scatter(x_train, y_train, label="Training data", color='b', alpha=.7)

# linear regression
LR = LinearRegression()
LR.fit(x_train.reshape(-1, 1), y_train.reshape(-1, 1))
prediction = LR.predict(x_test.reshape(-1, 1))

# just change 32 to whatever rank to show a prediction
# print("Prediction for rank 32")
# print(LR.predict(np.array([[32]]))[0])

print("Score for the model: ")

# one year arrays to compare linear regression to a single year
yxarr = numpy.array(yearx_values)
yyarr = numpy.array(yeary_values)

# score compared to single year
# score = LR.score(yxarr.reshape(-1, 1), yyarr)

# mean arrays to compare linear regression to means
xmarr = numpy.array(list(rankanddifferences.keys()))
ymarr = numpy.array(avgs)

#score compared to means
# score = LR.score(xmarr.reshape(-1, 1), ymarr)

# score against all year datapoints
score = LR.score(x_test.reshape(-1, 1), y_test)
print(score)

ax.plot(x_test, prediction, label='Predicted Differences', color='r')

# plot test data in scatter plot
# plt.scatter(x_test, y_test, label="Test Data", color='g', alpha=.7)

ax.scatter(xarr, yarr, label="Testing Data")

# ax.scatter(rankanddifferences.keys(), avgs, color='Red', label='Averages')


plt.title("RB Avg Difference in score vs Defensive Fantasy points allowed ranking")
plt.legend()
plt.show()
