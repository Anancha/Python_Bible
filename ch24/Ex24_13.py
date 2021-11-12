import pandas as pd
import matplotlib.pyplot as plt

my_df = { "sales" : [25550.49,35000.50,50020.85,
                     20000.00,15490.75],
          "cost" : [400,500,800,350,550]}
my_index = ["Perfume","Bag","Shoe","Man's clothes","Women's clothes"]
my_explode = [0.3,0,0,0,0]
my_colors = ["pink","orange","red","green","blue"]

df = pd.DataFrame(my_df,index=my_index)
plt.pie(df["sales"],labels=my_index)
plt.show()