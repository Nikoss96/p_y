import matplotlib.pyplot as mpl
import pandas as pd
import scipy.stats as sps
import numpy as np
from scipy import stats

#H_0 - оба банера выбирают одинаково часто
#H_A - обратное к H_0 => А или Б выбирается чаще конкурента

pack = pd.read_csv(r"C:\\Users\\nikch\\Desktop\\banner_click_stat.csv",sep = '\t')
pack.rename(columns = {'0':'A','0.1':'B'}, inplace = True)
#При считывании потеряли верхнюю строку, добавим
pack = pack.append({'A': '0' , 'B':'0'},ignore_index=True)  

sample_1 = pack['A']
sample_2 = pack['B']

print(stats.ttest_rel(sample_1.astype(int),sample_2.astype(int)))
print("\n")
for i in {1, 5}:
    if (stats.ttest_rel(sample_1.astype(int),sample_2.astype(int))[1])*100 > i:
        print("H_0 is correct for trust_int(%) =",i)
    else:
        print("H_0 is incorrect for trust_int(%) =",i)


#pack.split("")
#print(int(pack[0][0]))
#print(pack)