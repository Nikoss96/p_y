import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing
from sklearn.cluster import KMeans,DBSCAN
import datetime
import os
import seaborn as sns
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
import statsmodels.api as sm
frame = pd.read_csv('bank_transactions.csv')
#frame.drop(["TransactionID"],axis=1,inplace=True)
frame['TransactionDate'] = pd.to_datetime(frame['TransactionDate'])
med1 = frame.CustGender.mode().values[0]
med2 = frame.CustLocation.mode().values[0]
med3 = frame.CustAccountBalance.mode().values[0]
frame.CustGender.fillna(med1,inplace=True)
frame.CustLocation.fillna(med2,inplace=True)
frame.CustAccountBalance.fillna(med3,inplace=True)
y = str(int(pd.Series([int(i.split("/")[-1] ) for i in frame.CustomerDOB.dropna().values]).mode().values[0]))
d = str(int(pd.Series([int(i.split("/")[-3] ) for i in frame.CustomerDOB.dropna().values]).mode().values[0]))

m = str(int(pd.Series([int(i.split("/")[-2] ) for i in frame.CustomerDOB.dropna().values]).mode().values[0]))
frame.CustomerDOB.fillna(d + "/" + m + "/" + y,inplace=True)

ye = [int(i.split("/")[-1]) for i in frame.CustomerDOB.values]

mass = []
for i in ye:
    if(len(str(i))) == 4:
        mass.append(2022 - i)
    else:
        mass.append(2022 - (1900 + i))
frame["AllCustomerAge"] = mass     
sr = frame['AllCustomerAge'].median()
for i in range(len(mass)):
    if mass[i] > 115:
         mass[i] = sr
         
frame["AllCustomerAge"] = mass
plt.hist(mass,color='blue')
plt.xlabel("Age")
plt.title("Different ages")
plt.show()

frame = frame.loc[frame['CustGender'] != 'T']

#test_1 = frame.groupby('AllCustomerAge')['CustAccountBalance'].sum().plot(legend=True)
test_1 = frame.groupby('AllCustomerAge')['CustAccountBalance'].sum()

#test_2 = frame.groupby('CustLocation')['CustAccountBalance'].sum().plot(legend=True)
test_2 = frame.groupby('CustLocation')['CustAccountBalance'].sum()
add = frame.sort_values(['CustAccountBalance'],ascending=False).groupby('CustLocation')['CustAccountBalance'].sum()

#test_3 = frame.groupby('CustGender')['CustAccountBalance'].sum().plot(legend=True)
add1 = frame.sort_values(['CustAccountBalance'],ascending=False).groupby('CustGender')['CustAccountBalance'].sum()
plt.hist(add1,color='blue')
plt.xlabel("?")
plt.title("x")
plt.show()
frame['Gend'] = frame['CustGender']
frame.loc[(frame.Gend == "M"), ('Gend')] = 0
frame.loc[(frame.Gend == "F"), ('Gend')] = 1
variables = ['CustAccountBalance','TransactionAmount (INR)','AllCustomerAge']
#plt.figure(figsize=(8, 7))
#sns.heatmap(frame[variables].corr(), annot=True, cmap='Accent')

#model = sm.OLS(frame[variables]).fit()

scaler = StandardScaler()
up = scaler.fit_transform(frame[variables])

res = []

for k in range(1, 7):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(up)
    res.append(kmeans.inertia_)
    
plt.plot(range(1, 7), res,color = 'green')
plt.xticks(range(1, 7))
plt.xlabel('Variations')
plt.ylabel('Choosen stat m')
plt.show()
#
#kmeans = Means(clusters = 3)
#clusters count
kmeans = KMeans(n_clusters=3)
kmeans.fit(up)
res.append(kmeans.inertia_)
frame['NewClusters'] = kmeans.labels_

print(frame.groupby('NewClusters').agg({k: ['mean', 'median'] for k in variables}))

frame['Period'] = frame.TransactionDate.dt.strftime('%Y-%m')
frame['Cohort'] = frame.groupby(level=0)['TransactionDate'].min().dt.strftime('%Y-%m')

new = frame.groupby(['Cohort', 'Period'])
cohorts = new.agg({'CustomerID': pd.Series.nunique,'TransactionAmount (INR)': 'mean','TransactionID': 'count','AllCustomerAge': 'median'})
cohorts.rename(columns={'CustomerID': 'TotalClients','TransactionID': 'TotalOrders'}, inplace=True)

"""
  import matplotlib.pyplot as mpl
import pandas as pd
import scipy.stats as sps
import numpy as np
from scipy import stats
#H_0 avg pok speed = 66.6
#H_A - ~H_0 => avg speed <> 66.6
frame = pd.read_csv(r"User)))")

speed = frame['Speed']

# 1-side
print(stats.ttest_1samp(speed,66.6,alternative = 'greater'))
print("Average for speed sample:",speed.mean())
# mean ~ H_0
for i in {1, 5}:
    if (stats.ttest_1samp(speed,66.6,alternative = 'greater')[1])*100 > i:
        print("H_0 is correct for trust_int(%) =",i)
    else:
        print("H_0 is incorrect for trust_int(%) =",i)
        
import matplotlib.pyplot as mpl
import pandas as pd
import scipy.stats as sps
import numpy as np
import statsmodels as sm
from scipy import stats
#from statsmodels.stats.descriptivestats import sign_test
#import ipywidgets as widgets
#H_0 - медианное значение двух выборок не отличается (с точки зрения стат. значимости)
#H_A - ~H_0 => значительно различаются
frame = pd.read_csv(r"User))))")
sample_1 = frame[frame['version'] == 'gate_30']['sum_gamerounds']
sample_2 = frame[frame['version'] == 'gate_40']['sum_gamerounds']

print(sign_test(sample_1 - sample_2))

fr = frame.groupby('version')['sum_gamerounds'].median() 

delta = (fr.iloc[0].sum()-fr.iloc[1].sum())
print('При прямом сравнении выборок отличается на :', delta)


"""