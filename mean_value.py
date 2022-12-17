import matplotlib.pyplot as mpl
import pandas as pd
import scipy.stats as sps
import numpy as np
from scipy import stats
#import ipywidgets as widgets
#H_0 - среднее значение двух выборок не отличается (с точки зрения стат. значимости)
#H_A - ~H_0 => значительно различаются
frame = pd.read_csv(r"C:\\Users\\nikch\\Desktop\\cookie_cats.csv")
sample_1 = frame[frame['version'] == 'gate_30']['sum_gamerounds']
sample_2 = frame[frame['version'] == 'gate_40']['sum_gamerounds']

print(stats.ttest_ind(sample_1,sample_2,alternative = 'greater'))

for i in {1, 5}:
    if (stats.ttest_ind(sample_1,sample_2,alternative = 'greater')[1])*100 > i:
        print("H_0 is correct for trust_int(%) =",i)
    else:
        print("H_0 is incorrect for trust_int(%) =",i)
fr = frame.groupby('version')['sum_gamerounds'].mean() 

delta = (fr.iloc[0].sum()-fr.iloc[1].sum())
print('При прямом сравнении выборок отличается на :', delta)
