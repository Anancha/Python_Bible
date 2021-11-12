import pandas as pd
import matplotlib.pyplot as plt

my_df = { "day" : ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"],
          "temp_week1" : [6,8,6,8,10,8,6],
          "temp_week2" : [8,6,6,6,9,6,8],
          "temp_week3" : [10,9,10,8,7,9,8],
          "temp_week4" : [6,6,9,6,6,9,8]
        }
df = pd.DataFrame(my_df)
x = df["day"]
y1 = df["temp_week1"]
y2 = df["temp_week2"]
y3 = df["temp_week3"]
y4 = df["temp_week4"]

fig, ax = plt.subplots(nrows=2, ncols=2,figsize=(8,8),sharey=True)
ax[0,0].plot(x,y1,color="r",label="Temperature")
ax[0,0].legend(loc=2)
ax[0,1].plot(x,y2,color="g",label="Temperature")
ax[0,1].legend(loc="lower left")
ax[1,0].plot(x,y3,color="b",label="Temperature")
ax[1,0].legend(loc=10)
ax[1,1].plot(x,y4,color="c",label="Temperature")
ax[1,1].legend(loc="best")

ax[0,0].set_title("week1")
ax[0,1].set_title("week2")
ax[1,0].set_title("week3")
ax[1,1].set_title("week4")
plt.suptitle("Temperature on December (Celcius)")

fig.tight_layout()
plt.show()