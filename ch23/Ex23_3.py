import pandas as pd

tuple_data = ["red","green","green","blue","pink","blue"]
series1 = pd.Series(tuple_data, dtype="category", name="color")

print(series1)