import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

year = 2021

dstatsurl = 'https://www.pro-football-reference.com/years/'+ str(year) + '/opp.htm'

defdf = pd.read_html(dstatsurl)[0]

def calculateQBPtsAllowed(yds, td):
    return (yds/25) + (td*4)

def calculateReceivingPtsAllowed(yds ,td):
    return (yds/10) + (td*6)

def calculateReceivingPtsAllowedPPR(yds ,td, cmp):
    return (yds/10) + (td*6) + cmp

def calculateRushingPtsAllowed(yds, td):
    return (yds/10) + (td*6)


print("Defense Fantasy Stats")
# defdf.to_csv("2021def.csv")
defdf = defdf.rename(columns={'Unnamed: 1_level_0': 'Tm'})
defdf = defdf[:-3]

selection = defdf[[['Tm', 'Tm'], ['Passing', 'Cmp'], ['Passing', 'Yds'], ['Passing', 'TD'], ['Rushing', 'Yds'], ['Rushing', 'TD']]]
selection['TotalPtsAllowed', 'Passing'] = calculateQBPtsAllowed(selection['Passing', 'Yds'], selection['Passing', 'TD'])
selection['TotalPtsAllowed', 'Receiving'] = calculateReceivingPtsAllowed(selection['Passing', 'Yds'], selection['Passing', 'TD'])
selection['TotalPtsAllowed', 'ReceivingPPR'] = calculateReceivingPtsAllowedPPR(selection['Passing', 'Yds'], selection['Passing', 'TD'], selection['Passing', 'Cmp'])

selection['TotalPtsAllowed', 'Rushing'] = calculateRushingPtsAllowed(selection['Rushing', 'Yds'], selection['Rushing', 'TD'])

selection['Rank', 'ReceivingPPR'] = selection[('TotalPtsAllowed', 'ReceivingPPR')].rank(method='max', ascending=True)
selection['Rank', 'Receiving'] = selection[('TotalPtsAllowed', 'Receiving')].rank(method='max', ascending=True)
selection['Rank', 'Rushing'] = selection[('TotalPtsAllowed', 'Rushing')].rank(method='max', ascending=True)
selection['Rank', 'Passing'] = selection[('TotalPtsAllowed', 'Passing')].rank(method='max', ascending=True)
selection.to_csv("C:\\Users\\bluem\\vscodeprojects\FantasyAnalyzer\seasonaldefense\\"+str(year)+"def.csv")
# this just sorts it by whatever you want
selection = selection.sort_values(by=[('Rank', 'Rushing')], ascending=True)



print(selection)


