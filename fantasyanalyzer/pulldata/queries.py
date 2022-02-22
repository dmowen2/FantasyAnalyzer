import pandas as pd



# This file is for processing the different queries that be called through the command line functionality
class query:
    def __init__(self):
        self.generaldata = pd.read_csv("C:\\Users\\bluem\\vscodeprojects\FantasyAnalyzer\sheets\\fantasy2021.csv")
        # general sheets cleanup by replacing spaces
        self.generaldata.columns = [column.replace(" ", "_") for column in self.generaldata.columns]
        

    def queryPos(self, position):
        # position is a string value defining what position the individual fantasy player wants
        newdata = self.generaldata.query('Position == "%s"' % position)
        # fixing the display of the players
        self.data = newdata.groupby('Name').agg({'FantPt': ['mean', 'min', 'max']})

    def queryName(self, name):
        self.data = self.generaldata.query('Name == "%s"' % name)

    def queryTeam(self, teamabv):
        self.data = self.generaldata.query('Tm == "%s"' % teamabv)




        
    def printByFantPt(self):
        # This is sorted
        print(self.data.sort_values(by=('FantPt','min'), ascending=False))

    def printData(self):
        print(self.data)