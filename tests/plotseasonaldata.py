








from fantasyanalyzer.pulldata import queries, plotting
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# file for testing the ptAnalysis class and its individual functions regarding a single player


newQuery = queries.query("C:\\Users\\bluem\\vscodeprojects\FantasyAnalyzer\sheets\\2021seasonalfantasydata.csv")

newQuery.queryPos("RB", True)

hold = newQuery.getQuery().groupby('YINL').agg({'AvgFantPt': ['mean', 'min', 'max', 'std', 'sum']})
groups = list(newQuery.getQuery().groupby('YINL').groups.keys())
hold['YINL'] = groups
hold.to_csv('testdata.csv')

holdplot = hold.plot('YINL', ('AvgFantPt','mean'), style='o-', color='Red')
plt.title("RB Avg Fantasy Pts per YINL")
plt.show()

