import matplotlib.pyplot as mpl
import pandas as pd
import scipy.stats as sps
import numpy as np
from scipy import stats
#H_0 - default "grass" attack > default "rock" attack
#H_A - ~H_0
frame = pd.read_csv(r"C:\\Users\\nikch\\Desktop\\pokemon.csv")

grp = frame[frame['Class 1'] == 'Grass']['Attack']
rop = frame[frame['Class 1'] == 'Rock']['Attack']
print(stats.ttest_ind(grp,rop,alternative = 'greater'))
if (stats.ttest_ind(grp,rop,alternative = 'greater')[1])*100 > 5:
    print("H_0 is correct")
else:
    print("H_0 is incorrect")