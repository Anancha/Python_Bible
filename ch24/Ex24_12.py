import pandas as pd
import matplotlib.pyplot as plt

my_df = { "Year": ["2019", "2020", "2021", "2022", "2023"],
          "NotebookA1" : [20,22,25,20,18],
          "NotebookA2" : [30,40,30,35,40],
          "NotebookA3" : [15,10,26,23,27]
        }
df = pd.DataFrame(my_df,columns=["Year","NotebookA1","NotebookA2","NotebookA3"])
plt.stackplot(df["Year"],df["NotebookA1"], df["NotebookA2"],df["NotebookA3"],
              colors =["#0000FF", "#FFA500","#00FF00"])
plt.show()