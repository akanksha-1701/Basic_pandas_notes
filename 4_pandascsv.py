# # read csv files:(comma seperated file)
# #  it is simple way to store the big and bigest data sets.
# # csv files contains plain text and is a well know format that can be read by everyone including Pandas.
# # loding the csv into a dataframe
import pandas as pd
df=pd.read_csv('data.csv')
print(df.to_string())  #use to_string() to print the entire DataFrame.

# # Print the DataFrame without the to_string() method:
import pandas as pd
df = pd.read_csv('data.csv')
print(df) 


# max_rows
# The number of rows returned is defined in Pandas option settings.
# You can check your system's maximum rows with the pd.options.
# display.max_rows statement.
import pandas as pd
print(pd.options.display.max_rows)

# Increase the maximum number of rows to display the entire DataFrame:
import pandas as pd
pd.options.display.max_rows=9999
df = pd.read_csv('data.csv')
print(df) 