import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

my_df = { "day" : ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"],
          "temp_week1" : [6,8,6,8,10,8,6],
          "temp_week2" : [8,6,6,6,9,6,8]
        }
df = pd.DataFrame(my_df)
x = df["day"]
y1 = df["temp_week1"]
y2 = df["temp_week2"]
plt.title("Temperature 2 weeks (Celcius)")
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.plot(x,y1,color="r")
plt.plot(x,y2,color="b")
plt.show()