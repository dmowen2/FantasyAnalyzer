import pandas as pd



# This file is for processing the different queries that be called through the command line functionality
class query:
    def __init__(self, csvtoread="C:\\Users\\bluem\\vscodeprojects\FantasyAnalyzer\sheets\\fantasy2021.csv"):
        basequery = "C:\\Users\\bluem\\vscodeprojects\FantasyAnalyzer\sheets\\fantasy2021.csv"
        self.generaldata = pd.read_csv(csvtoread)
        self.data = self.generaldata
        # general sheets cleanup by replacing spaces
        self.generaldata.columns = [column.replace(" ", "_") for column in self.generaldata.columns]
        

    def queryPos(self, position, seasonal=False):
        # position is a string value defining what position the individual fantasy player wants
        self.data = self.generaldata.query('Position == "%s"' % position)
        # fixing the display of the players
        # working line
        if seasonal == False:
            self.data = self.data.groupby('Name').agg({'FantPt': ['mean', 'min', 'max', 'std', 'sum']})
            self.data['Name'] = self.generaldata['Name']
        # Test line

        # self.data = newdata.groupby('Name').agg(['mean', 'min', 'max', 'std', 'sum'])



    # Makes a query/finds the player based on the name taken in as an input
    def queryName(self, name):
        self.data = self.generaldata.query('Name == "%s"' % name)

    # Makes a query/finds the player based on the name of the team taken in as an input
    def queryTeam(self, teamabv):
        self.data = self.generaldata.query('Tm == "%s"' % teamabv)


    # Saves the data the path needs to be changed depending on where this is stored on the device
    def saveData(self, name):
        path = "C:\\Users\\bluem\\vscodeprojects\FantasyAnalyzer\sheets\\" + name + ".csv"
        self.data.reset_index
        self.data.to_csv(path)
        print("Saved")


    # Returns the data saved in the query
    def getQuery(self):
        return self.data


    # Makes a new column in the data frame based on user input proceeds to rank the column u want inputed and puts it in that column
    def rankby(self):
        # new column name is the column name u want to add, rank column is
        newcolumnname = input("Insert the name of the column to be added: ")
        rankcolumn = input("Insert the name of the column you want ranked by: ")

        # true input needs to given for the ranks in order
        ascend = input("Ascending (True/False) (WARNING for Ranked Data type \"true\"): ")
        ascent = False
        if ascend.lower() == 'true':
            ascent = True
        try:

            self.data[newcolumnname] = self.data[rankcolumn].rank(method='max', ascending=ascent)
        except:
            # ascent needs to be false to rank highest value to lowest rank
            self.data[newcolumnname] = self.data['FantPt'][rankcolumn].rank(method='min', ascending=ascent)


    """ Takes the average value between two individual colums, mostly used to average the rank between two separate
     columns """

    def averageColumns(self):
        # Should probably be improved to take a multitude of columns rather than just 2 have the user input
        # the amount of columns they want to add then ask the amount of questions necessary for it
        col1 = input('Insert Column 1 you want to average: ')
        col2 = input('Insert Column 2 you want to average: ')
        print("Creating column: " + 'avg'+col1+col2)
        self.data['avg'+col1+col2] = self.data[[col1, col2]].mean(axis=1)




    def printByFantPt(self):
        # This is sorted
        # Might have to trim the mean by excluding outliers
        # Have to input a way of adding additional columns to what is being asked within the input statement
        whattosortby = input("What would you like to sort by? ('mean', 'std', 'min', 'max')")
        try:
            print(self.data.sort_values(by=('FantPt',whattosortby), ascending=False))
        except:
            print(self.data.sort_values(by=(whattosortby), ascending=False))

    def printData(self):
        print(self.data)