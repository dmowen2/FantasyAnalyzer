import pandas

from fantasyanalyzer.pulldata import queries, plotting
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# file for testing the ptAnalysis class and its individual functions regarding a single player
years = [2012, 2013, 2014, 2015, 2016, 2017,2018, 2019, 2020, 2021]

avgline = pandas.DataFrame(columns=years)

yinl = {0: [0, 0], 1: [0, 0], 2: [0, 0], 3: [0, 0], 4: [0, 0], 5: [0, 0], 6: [0, 0], 7: [0, 0], 8: [0, 0], 9: [0, 0], 10: [0, 0], 11: [0, 0], 12: [0, 0], 13: [0, 0], 14: [0, 0], 15: [0, 0], 16: [0, 0]}


for year in years:
    newQuery = queries.query("C:\\Users\\bluem\\vscodeprojects\FantasyAnalyzer\seasonalsheets\\"+str(year)+"seasonalfantasydata.csv")

    newQuery.queryPos("RB", True)

    hold = newQuery.getQuery().groupby('YINL').agg({'AvgFantPt': ['mean', 'min', 'max', 'std', 'sum']})
    groups = list(newQuery.getQuery().groupby('YINL').groups.keys())

    hold['YINL'] = groups

    for yinlnum in groups:
            yinl[yinlnum][0] += hold[('AvgFantPt', 'mean')][yinlnum]
            yinl[yinlnum][1] += 1
    # hold.to_csv('testdata.csv')

    # remove this line or comment it out to simply plot the avg mean
    plt.plot(hold['YINL'], hold[('AvgFantPt','mean')], label=str(year))

avgvalue = []
for k in yinl:
    avgvalue += [yinl[k][0]/yinl[k][1]]

# plots the average of each individual subplot
plt.plot(yinl.keys(), avgvalue, label="Avg Mean",color='Blue')

plt.ylabel("Mean Fantasy Points")
plt.xlabel("Years in league")
plt.title("10 Year RB Years In League vs Mean Fantasy Points Data")
plt.legend()
plt.show()

