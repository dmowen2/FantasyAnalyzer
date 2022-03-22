
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

"""
Example input
    Insert the name of the column to be added: meanr
    Insert the name of the column you want ranked by: mean
    Ascending (True/False): f
    Insert the name of the column to be added: sumr
    Insert the name of the column you want ranked by: sum
    Ascending (True/False): f
    Insert Column 1 you want to average: meanr
    Insert Column 2 you want to average: sumr
    Creating column: avgmeanrsumr
    Insert the name of the column to be added: rank
    Insert the name of the column you want ranked by: avgmeanrsumr
    Ascending (True/False): True
    What would you like to sort by? ('mean', 'std', 'min', 'max')avgmeanrsumr
"""