import pandas as pd

name = ["นายเอ", "นางสาวบี", "นายซี"]
salary = [18000,25000,35000]

# สร้างดิกชันนารีจากลิสต์
data = {"ชื่อ":name,"เงินเดือน":salary}

df = pd.DataFrame(data)
print(df)