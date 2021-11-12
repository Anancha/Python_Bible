import pandas as pd

list_data = [3.83,4.00,2.98,3.00,2.80]
series1 = pd.Series(list_data, index = ["A","A","B","A","B"])
print(series1)