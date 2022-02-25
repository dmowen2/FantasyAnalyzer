

class ptAnalysis:
    def __init__(self, df, name=''):
        self.df = df
        self.name = name

    # converts a dataframe to a list this can probably be moved to a different class
    def dfToList(self, df):
        dflst = df.values.tolist()
        print(dflst)

    def processPts(self):
        self.pts = self.df['FantPt']
        self.mean = self.pts.mean()
        self.std = self.pts.std()
        return self.pts

# Need to develop some sort of scoring system that will score the individual based on mean and having a low standard
# deviation

    def printAnalysis(self):
        print(self.name + "\nMean: " + str(round(self.mean, 2)) + "\nStandard Deviation: " + str(round(self.std, 2)))