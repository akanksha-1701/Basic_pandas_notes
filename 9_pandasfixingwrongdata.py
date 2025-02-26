# wrong Data: its only a wrong data
# "Wrong data" does not have to be "empty cells" or "wrong format", it can just be wrong, like if someone registered "199" instead of "1.99".
# loading and reading the original dataframe
import pandas as pd
sharad = pd.read_csv('dirtydata.csv')
print(sharad.to_string())

# here we will set "Duration" = 45 in row 7:
import pandas as pd
sharad = pd.read_csv('dirtydata.csv')
sharad.loc[7,'Duration'] = 45
print(sharad.to_string())

# for larger data set: now here we will loop through all the values in "Duration" column, if the value is higher than 120 than set it to 120.
import pandas as pd
sharad = pd.read_csv('dirtydata.csv')
for i in sharad.index:
    if sharad.loc[i, "Duration"] > 120:
        sharad.loc[i, "Duration"] = 120
print(sharad.to_string())

# you can also remove the rows for wrong data in larger dataset.
import pandas as pd
sharad = pd.read_csv('dirtydata.csv')
for i in sharad.index:
    if sharad.loc[i, "Duration"] > 120:
        sharad.drop(i, inplace=True)
print(sharad.to_string())