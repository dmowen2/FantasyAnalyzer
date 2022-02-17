import pandas as pd

data = pd.read_csv("C:\\Users\\bluem\PycharmProjects\\fantasymessaround\\fantasy2021.csv")

# replacing blank spaces with '_'
data.columns = [column.replace(" ", "_") for column in data.columns]

# filtering with query method

newdata = data.query('Position == "%s"' % "TE")

# display


groupedbyplayername = newdata.groupby('Name').agg({'FantPt': ['mean', 'min', 'max']})


print(groupedbyplayername.sort_values(by=('FantPt','min'), ascending=False))