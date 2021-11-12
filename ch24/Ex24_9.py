import pandas as pd
import matplotlib.pyplot as plt

df = { "month" : ["Jan", "Feb" , "Mar"],
       "sales" : [20000, 25000 , 90000]
     }
my_df = pd.DataFrame(df)
x = df["month"]
y = df["sales"]
plt.bar(x,y,align="edge",alpha=0.3)
plt.title("Sales Quarter1 2021")
plt.xlabel("month")
plt.ylabel("Sales volume")
plt.show()