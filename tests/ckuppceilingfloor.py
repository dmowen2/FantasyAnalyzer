import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

ckuppurl = 'https://www.pro-football-reference.com/players/K/KuppCo00/gamelog/2021/'

#stores it as a pandas dataframe
ckuppdf = pd.read_html(ckuppurl)[0]
#df.to_csv('CooperKupp.csv') - stores this as a csv file

#this prints the length of the dataframe created by pandas ***rows*** as in downwards
#print(len(ckuppdf))

#makes a list of all the individual columns within the dataframe separates them into their separate specific names
#print(list(ckuppdf.columns))

#game played and then targets?
#print(ckuppdf['Receiving', 'Tgt'])

print("Cooper Kupp Fantasy Stats")



def fantasyptscalc(cyd, ryd, pts):
    return cyd/10 + ryd/10 + pts

def pprptscalc(rec, cyd, ryd, pts):
    return rec + cyd/10 + ryd/10 + pts



selection = ckuppdf[[['Receiving', 'Rec'], ['Receiving', 'Yds'], ['Rushing', 'Yds'], ['Scoring', 'Pts']]]
selection['Fantasy Pts', 'Non-PPR'] = fantasyptscalc(selection['Receiving', 'Yds'], selection['Rushing', 'Yds'], selection['Scoring', 'Pts'])
selection['Fantasy Pts', 'PPR'] = pprptscalc(selection['Receiving', 'Rec'], selection['Receiving', 'Yds'], selection['Rushing', 'Yds'], selection['Scoring', 'Pts'])


print(selection)

totalgames = 17



totalcyds = ckuppdf['Receiving', 'Yds'][17]

#print("Cooper Kupp Total Receiving Yds: ", totalcyds)
avgyds = totalcyds/totalgames
#print("Cooper Kupp Average Receiving Yds: ", avgyds)
#print()
totalpts = ckuppdf['Scoring', 'Pts'][17]

#print("Cooper Kupp Total Pts Scored: ", totalpts)
avgpts = totalpts/totalgames
#print("Cooper Kupp Average Pts Scored: ", avgpts)
#print()
#total rush yards
totalryds = ckuppdf['Rushing', 'Yds'][17]

#total receptions
totalrec = ckuppdf['Receiving', 'Rec'][17]

fantasypts = (totalcyds/10) + (totalryds/10) + totalpts
fantasyptsavg = fantasypts/totalgames
print("Cooper Kupp Total Fantasy Pts Scored: ", fantasypts)
print("Cooper Kupp Average Fantasy Pts Scored: ", fantasyptsavg)

removetotal = selection['Fantasy Pts', 'Non-PPR'].drop([0, 17])
print("Cooper Kupp Pt Max: ", removetotal.max())
print("Cooper Kupp Pt Min: ", removetotal.min())
print("Cooper Kupp Pt Standard Deviation: ", removetotal.std())
print("Cooper Kupp Coefficient of Variance: ", (removetotal.std()/fantasyptsavg)*100)

print()

pprpts = (totalcyds/10) + (totalryds/10) + totalpts + totalrec
ppravg = pprpts/totalgames
print("Cooper Kupp Total PPR Fantasy Pts Scored: ", pprpts)
print("Cooper Kupp Average PPR Fantasy Pts Scored: ", ppravg)

ppremovetotal = selection['Fantasy Pts', 'PPR'].drop([0, 17])
print("Cooper Kupp Pt Max: ", ppremovetotal.max())
print("Cooper Kupp Pt Min: ", ppremovetotal.min())
print("Cooper Kupp Pt Standard Deviation: ", ppremovetotal.std())
print("Cooper Kupp Coefficient of Variance: ", (ppremovetotal.std()/fantasyptsavg)*100)

print()
