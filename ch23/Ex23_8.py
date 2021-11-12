import pandas as pd

name_series = pd.Series(["สมชาย","สมหญิง","สมใจ"])
surname_series = pd.Series(["รักธรรม","ใจดี","ใฝ่ดี"])
age_series = pd.Series([18,19,20])

name_df = pd.DataFrame(name_series,columns=["ชื่อ"])
surname_df = pd.DataFrame(surname_series,columns=["นามสกุล"])
age_df = pd.DataFrame(age_series,columns=["อายุ"])

df = pd.concat([name_df,surname_df,age_df],axis=1)
print(df)