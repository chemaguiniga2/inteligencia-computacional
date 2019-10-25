import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pylab as plt

data = pd.read_csv("examen.csv")
correlation = data.corr()
correlation = np.abs(correlation)
print(correlation)
graph = sns.heatmap(correlation, cmap=sns.color_palette('Blues'))
plt.show()
