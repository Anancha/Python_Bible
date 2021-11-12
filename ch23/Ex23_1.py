import pandas as pd

list_data = [3.83,4.00,2.98,3.00,2.80]
series1 = pd.Series(list_data,name="Series1")
print(series1)
print()

series2 = pd.Series([98,100,78,80,70],name="Series2")
print(series2)