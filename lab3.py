import matplotlib.pyplot
import pandas as pd
import seaborn as sns
from matplotlib import rcParams


infile = "https://raw.githubusercontent.com/grbruns/cst383/master/campaign-ca-2016-sample.csv"
df = pd.read_csv(infile)

print(df)

#3
#Column contb_receipt_amt looks like it is numeric and also file_num as well. I would have thought that
#cmte_id and cand_id would also be numeric since they are ID files.

#4
#Receipt_desc and memo_cd contain mostly nan values. Memo_text has a few nan as well.

#5
#The column memo_cd is mostly filled with nan but has a few rows marked with X which I assume is empty.

#6
#There are a few values of contbr_occupation that could be set to nan such as retired, not employed and retired.

#7
#A lot of the terms could be grouped better or simply not used, retired, disabled, none, and not employed are all the same essentially.

#8
#Memo_cd only contains nan and 2 rows of X.

