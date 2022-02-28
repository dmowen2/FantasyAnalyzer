
from fantasyanalyzer.main import ptAnalysis
from fantasyanalyzer.pulldata import queries


# file for testing the ptAnalysis class and its individual functions regarding a single player

newQuery = queries.query()
newQuery.queryPos("TE")
queryhold = newQuery.getQuery()


#testing data
newQuery.rankby()
newQuery.rankby()
# rank by creates a new column with the values ranked by the highest scoring value from the data set
# Asks ascending true or false based on....

newQuery.averageColumns()
# takes two columns and averages their values together into another column
#


newQuery.rankby()

newQuery.printByFantPt()

# newQuery.saveData("tedata")