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
frame = pd.read_csv(r"C:\\Users\\nikch\\Desktop\\cookie_cats.csv")
sample_1 = frame[frame['version'] == 'gate_30']['sum_gamerounds']
sample_2 = frame[frame['version'] == 'gate_40']['sum_gamerounds']

print(sign_test(sample_1 - sample_2))

fr = frame.groupby('version')['sum_gamerounds'].median() 

delta = (fr.iloc[0].sum()-fr.iloc[1].sum())
print('При прямом сравнении выборок отличается на :', delta)