import pandas as pd

tuple_data = ("red","green","blue","pink")
series1 = pd.Series(tuple_data, index=("r","g","b","p"), name="color")

print(series1)