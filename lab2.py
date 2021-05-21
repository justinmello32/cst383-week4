import pandas
import pandas as pd
import seaborn as sns
from matplotlib import rcParams

# allow output to span multiple output lines in the console
pd.set_option('display.max_columns', 500)

# switch to seaborn default stylistic parameters
# see the useful https://seaborn.pydata.org/tutorial/aesthetics.html
sns.set()
sns.set_context('paper') # 'talk' for slightly larger

# change default plot size
rcParams['figure.figsize'] = 9,7

#1
df = pd.read_csv("https://raw.githubusercontent.com/grbruns/cst383/master/airquality.csv")

#2
print(df[:1])

#3
print(df.dtypes)

#4
print(df.isna().sum())
print(df.isna().mean())

#5
print(df.isna().sum().count())