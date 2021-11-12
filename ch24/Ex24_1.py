import pandas as pd
import matplotlib.pyplot as plt

my_df = { "day" : ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"],
          "temperature (celcius)" : [6,8,6,8,10,8,6]
        }
df = pd.DataFrame(my_df)
x = df["day"]
y = df["temperature (celcius)"]
plt.plot(x,y)
plt.show()