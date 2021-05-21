import matplotlib.pyplot
import pandas
import pandas as pd
import seaborn as sns
from matplotlib import rcParams
from scipy.stats import zscore

wine = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", sep=";")
#1
print(wine)

#2
wine_sample = wine.sample(n=20)
print(wine_sample)

#3
z_normalization = zscore(wine_sample)

#4
print(z_normalization.min())

#5
print(z_normalization.max())

#6
unit_interval_normalization = (wine_sample - wine_sample.min())/(wine_sample.max() - wine_sample.min())
print(unit_interval_normalization)

#7
print(unit_interval_normalization.min())
print(unit_interval_normalization.max())

#8
df = wine
print(df.corr())