
from fantasyanalyzer.main import ptAnalysis
from fantasyanalyzer.pulldata import queries


# file for testing the ptAnalysis class and its individual functions regarding a single player

newQuery = queries.query()
newQuery.queryPos("TE")
queryhold = newQuery.getQuery()


#testing data
newQuery.rankby()
newQuery.rankby()
newQuery.averageColumns()
newQuery.rankby()

newQuery.printByFantPt()

# newQuery.saveData("tedata")