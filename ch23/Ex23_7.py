import pandas as pd

name_series = pd.Series(["สมชาย","สมหญิง","สมใจ"])
df = pd.DataFrame(name_series,columns=["ชื่อ"])
print(df)