# Data Cleaning
# Data cleaning means fixing bad data in your data set.
# Bad data could be:
# Empty cells
# Data in wrong format
# Wrong data
# Duplicates
# In this tutorial you will learn how to deal with all of them.
## Empty Cells
# Empty cells can potentially give you a wrong result when you analyze data.
import pandas as pd
Akanksha=pd.read_csv('data.csv')
print(Akanksha.to_string())
# # # Remove Rows
# # # One way to deal with empty cells is to remove rows that contain empty cells.
# # here we will return a new dataframe with no empty cell.
import pandas as pd
Akanksha=pd.read_csv('data.csv')
Akankshanew=Akanksha.dropna()
print(Akankshanew.to_string())

# # By default, the dropna() method returns 
# # a new DataFrame, and will not change the original.
# # If you want to change the original DataFrame, use the inplace = True argument:
import pandas as pd 
Akanksha=pd.read_csv('data.csv')
Akanksha.dropna(inplace=True)
print(Akanksha.to_string())

# # Replace Empty Values
# # Another way of dealing with empty cells is to insert a new value instead.
# # This way you do not have to delete entire rows just because of some empty cells.
# # The fillna() method allows us to replace empty cells with a value:
import pandas as pd 
df=pd.read_csv('data.csv')
df.fillna(130,inplace=True)
print(df.to_string())
# # Replace Only For Specified Columns
# # The example above replaces all empty cells in the whole Data Frame.
# # To only replace empty values for one column, specify the column name for the DataFrame:
import pandas as pd
df = pd.read_csv('data.csv')
df["Calories"].fillna(130, inplace = True)
print(df.to_string())
# # Replace Using Mean, Median, or Mode
# # A common way to replace empty cells, is to calculate the mean, median or mode value of the column.
# # Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:

# # Mean = the average value (the sum of all values divided by number of values).
import pandas as pd
df = pd.read_csv('data.csv')
x = df["Calories"].mean()
df["Calories"].fillna(x, inplace = True)
print(df.to_string())
# # Median = the value in the middle, after you have sorted all values ascending.
import pandas as pd
df = pd.read_csv('data.csv')
x = df["Calories"].median()
df["Calories"].fillna(x, inplace = True)
print(df.to_string())
# # Mode = the value that appears most frequently.
import pandas as pd
df = pd.read_csv('data.csv')
x = df["Calories"].mode()[0]
df["Calories"].fillna(x, inplace = True)
print(df.to_string())
