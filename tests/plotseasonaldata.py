








from fantasyanalyzer.pulldata import queries, plotting
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# file for testing the ptAnalysis class and its individual functions regarding a single player


newQuery = queries.query("C:\\Users\\bluem\\vscodeprojects\FantasyAnalyzer\sheets\\2021seasonalfantasydata.csv")

newQuery.queryPos("RB", True)

print(newQuery.getQuery())
hold = newQuery.getQuery().plot.scatter('AvgFantPt', 'YINL', 5, 'Red')

plt.show()

