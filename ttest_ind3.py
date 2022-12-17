import matplotlib.pyplot as mpl
import pandas as pd
import scipy.stats as sps
import numpy as np
from scipy import stats
#H_0 avg pok speed = 66.6
#H_A - ~H_0 => avg speed <> 66.6
frame = pd.read_csv(r"C:\\Users\\nikch\\Desktop\\pokemon.csv")

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