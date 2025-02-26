##Pandas DataFrames
# A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
#load data into a DataFrame object:
df = pd.DataFrame(data)
print(df) 

# locate row: pandas use the loc attibute to return one or more specified row.
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
#load data into a DataFrame object:
df = pd.DataFrame(data)
print(df.loc[0]) 
# example of returning row 0 and 1
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
#load data into a DataFrame object:
df = pd.DataFrame(data)
print(df.loc[[0,1]]) 

# name index: with the index you can name your own indexes.
import pandas as pd
data = {
  "cal": [420, 380, 390],
  "dur": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df) 

# located the name inssdex
import pandas as pd
data = {
  "cal": [420, 380, 390],
  "dur": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df.loc["day2"]) 

# output in a dataframe 
import pandas as pd
data = {
  "cal": [420, 380, 390],
  "dur": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df.loc[["day1","day2"]]) 

Load Files Into a DataFrame-
If your data sets are stored in a file, Pandas can load them into a DataFrame.

import pandas as pd

df = pd.read_csv('data.csv')

print(df) 