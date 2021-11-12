import pandas as pd

dict_data = {"Mon":"Monday","Tue":"Tuesday","Wed":"Wednesday","Thu":"Thursday","Fri":"Friday","Sat":"Saturday","Sun":"Sunday"}
series1 = pd.Series(dict_data)
print(series1)