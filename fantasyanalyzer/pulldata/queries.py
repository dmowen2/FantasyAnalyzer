from turtle import pos
import pandas as pd




class query:
    def __init__(self):
        self.generaldata = pd.read_csv("..\\..\\fantasy2021.csv")
        
        # general data cleanup by replacing spaces
        self.generaldata.columns = [column.replace(" ", "_") for column in self.generaldata.columns]
        

    def queryPos(self, position):
        # position is a string value defining what position the individual fantasy player wants
        self.newdata = self.generaldata.query('Position == "%s"' % position)
        # fixing the display of the players
        self.groupedbyplayername = self.newdata.groupby('Name').agg({'FantPt': ['mean', 'min', 'max']})
        
    def printByFantPt(self):
        print(self.groupedbyplayername.sort_values(by=('FantPt','min'), ascending=False))