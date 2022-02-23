from fantasyanalyzer.main import ptAnalysis
from fantasyanalyzer.pulldata import queries


# file for testing the ptAnalysis class and its individual functions regarding a single player

newQuery = queries.query()
name = input("Please enter the name of the player you would like to query: ")
newQuery.queryName(name)
queryhold = newQuery.getQuery()
processquery = ptAnalysis.ptAnalysis(queryhold, name)
processquery.dfToList(processquery.processPts())
processquery.printAnalysis()