import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

my_df = { "day" : ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"],
          "temperature (celcius)" : [6,8,6,8,10,8,6]
        }
df = pd.DataFrame(my_df)
x = df["day"]
y = df["temperature (celcius)"]
plt.plot(x,y,linestyle="-",linewidth=0.8)
plt.title("Temperature around this week (Celcius)")
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.xticks(rotation=65)
plt.yticks(np.arange(5,15,1))
plt.show()