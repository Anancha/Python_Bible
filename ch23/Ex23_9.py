import pandas as pd

data = [["นายเอ", 18000], ["นางสาวบี", 25000], ["นายซี", 35000]]

df = pd.DataFrame(data, columns=["ชื่อ", "เงินเดือน"])
print(df)