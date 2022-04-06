import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class plotting:
    def __init__(self, data):
        self.data = data

    # random color function stolen from stack overflow
    def get_cmap(self, n, name='hsv'):
        return plt.cm.get_cmap(name, n)


    # Function that simply allows users to input the necessary details for a scatterplot
    def scatterplot(self):
        title = input("Enter a title for the graph: ")
        print("Enter X and Y axis's")
        col1 = input("Enter the column name for the X axis: ")
        col2 = input("Enter the column name for the Y axis:  ")

        # modifying the dataframe so it is easier to annotate and add labels to the scatterplot
        # modifydf = self.data[[('FantPt', col1), ('FantPt', col2)]].copy()
        # print(modifydf)

        # error being thrown right here
        x = len(self.data[('FantPt', col1)])
        hold = self.data.plot.scatter(('FantPt', col1), ('FantPt', col2),5, np.random.rand(x,3))
        # annotate the individual rows/label each data point on the graph with the corresponding player name

        for k, v in self.data.iterrows():

            plt.annotate(k, (v[('FantPt', col1)], v[('FantPt', col2)]))

        plt.title(title)
        plt.xlabel(col1)
        plt.ylabel(col2)


        plt.show()