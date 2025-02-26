# # A Pandas Series is like a column in a table. It is a one-dimensional array holding data of any type.
# # here we will create a simple pandas serie
# s.
import pandas as pd

Akanksha=[1,7,2]
myvar=pd.Series(Akanksha)
print(myvar)

print(myvar[0])

# # labeling -label can be use to  access a specified
import pandas as pd
Akanksha =[1,7,2]
myvar=pd.Series(Akanksha)
print(myvar[0])
# # with create lable you can create your own name lables:
import pandas as pd
Akanksha=[1,7,2]
myvar=pd.Series(Akanksha, index=["x","y","z"])
print(myvar)
# # labeling - label can be use to access a specified value .(after creating own label)
import pandas as pd
Akanksha=[1,7,2]
myvar=pd.Series(Akanksha, index=["x","y","z"])
print(myvar["x"])


# # you can also use a key or value object like  a dictionary, when creating a Series.
# # here we will create a simple pandas series from a dictionary.
import pandas as pd 
cal = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(cal)
print(myvar)

# # Create a Series using only data from "day1" and "day2":
import pandas as pd
cal = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(cal, index = ["day1", "day2"])
print(myvar)

# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
# Series is like a column, a DataFrame is the whole table.
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar)