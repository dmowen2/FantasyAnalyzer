import matplotlib.pyplot as plt
from fantasyanalyzer.main import ptAnalysis
from fantasyanalyzer.pulldata import queries, plotting



# file for testing the ptAnalysis class and its individual functions regarding a single player


newQuery = queries.query()

newQuery.queryPos("TE")
'''
queryhold = newQuery.getQuery()


#testing data
newQuery.rankby()
newQuery.rankby()
# rank by creates a new column with the values ranked by the highest scoring value from the data set
# Asks ascending true or false based on....
'''

# newQuery.saveData("tedata")

plotting = plotting.plotting(newQuery.getQuery())
plotting.scatterplot()

'''
newQuery.getQuery().plot.scatter("meanr", "sumr",5, "Red")
plt.title("TE Mean vs Sum Data")
plt.show()
'''