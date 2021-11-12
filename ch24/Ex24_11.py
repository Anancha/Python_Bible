import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

my_df = { "Quarter" : ["Q1","Q2","Q3","Q4"],
          "SalesOfProd1" : [60000,80000,125000,78500],
          "SalesOfProd2" : [93650,35300,47550,38550]
        }
df = pd.DataFrame(my_df)
plt.figure(figsize=[10,8])
plt.grid()
plt.plot(df["Quarter"],df["SalesOfProd1"],marker="s",ls="-.",
         lw=3,ms=10,mec="blue",mfc="cyan",label="product1")
plt.plot(df["Quarter"],df["SalesOfProd2"],color="red",marker="*",
         ls="--",lw=3,ms=15,mfc="#E8CCD7",label="product2")
plt.xticks(rotation=45)
plt.yticks(np.arange(30000,130000,5000))
plt.legend(loc="lower left")
plt.xlabel("Quarter")
plt.ylabel("Sales")
plt.title("Sales per quarter")
plt.show()