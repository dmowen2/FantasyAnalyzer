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
        self.data = newdata.groupby('Name').agg({'FantPt': ['mean', 'min', 'max', 'std', 'sum']})



    def queryName(self, name):
        self.data = self.generaldata.query('Name == "%s"' % name)

    def queryTeam(self, teamabv):
        self.data = self.generaldata.query('Tm == "%s"' % teamabv)

    def saveData(self, name):
        path = "C:\\Users\\bluem\\vscodeprojects\FantasyAnalyzer\sheets\\" + name + ".csv"
        self.data.reset_index
        self.data.to_csv(path)
        print("Saved")


    def getQuery(self):
        return self.data



    def rankby(self):
        # new column name is the column name u want to add, rank column is
        newcolumnname = input("Insert the name of the column to be added: ")
        rankcolumn = input("Insert the name of the column you want ranked by: ")
        ascend = input("Ascending (True/False): ")
        ascent = False
        if ascend.lower() == 'true':
            ascent = True
        try:

            self.data[newcolumnname] = self.data[rankcolumn].rank(method='max', ascending=ascent)
        except:
            # ascent needs to be false to rank highest value to lowest rank
            self.data[newcolumnname] = self.data['FantPt'][rankcolumn].rank(method='min', ascending=ascent)

    def averageColumns(self):
        col1 = input('Insert Column 1 you want to average: ')
        col2 = input('Insert Column 2 you want to average: ')
        print("Creating column: " + 'avg'+col1+col2)
        self.data['avg'+col1+col2] = self.data[[col1, col2]].mean(axis=1)



    def printByFantPt(self):
        # This is sorted
        # Might have to trim the mean by excluding outliers
        whattosortby = input("What would you like to sort by? ('mean', 'std', 'min', 'max')")
        try:
            print(self.data.sort_values(by=('FantPt',whattosortby), ascending=False))
        except:
            print(self.data.sort_values(by=(whattosortby), ascending=False))

    def printData(self):
        print(self.data)