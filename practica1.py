import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pylab as plt

data=pd.read_csv('/Users/josemariaaguinigadiaz/Desktop/Inteligencia Computacional/twitter.csv')
correlation=data.corr()
correlation=np.abs(correlation)
graph=sns.heatmap(correlation, cmap=sns.color_palette("Blues"))
plt.show()