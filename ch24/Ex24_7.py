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

# สร้าง axes 4 ตัวบน figure แบ่งเป็น 2 แถว 2 คอลัมน์
fig, ax = plt.subplots(nrows=2, ncols=2,figsize=(5,5),sharey=True)
# พล๊อตกราฟแถวที่ 1 คอลัมน์ที่ 1
ax[0,0].plot(x,y1,color="r")
ax[0,0].set_ylabel("Temperature")
# พล๊อตกราฟแถวที่ 1 คอลัมน์ที่ 2
ax[0,1].plot(x,y2,color="g")
# พล๊อตกราฟแถวที่ 2 คอลัมน์ที่ 1
ax[1,0].plot(x,y3,color="b")
ax[1,0].set_xlabel("Day")
ax[1,0].set_ylabel("Temperature")
# พล๊อตกราฟแถวที่ 2 คอลัมน์ที่ 2
ax[1,1].plot(x,y4,color="c")
ax[1,1].set_xlabel("Day")
# เซตค่า title ของแต่ละ axes
ax[0,0].set_title("week1")
ax[0,1].set_title("week2")
ax[1,0].set_title("week3")
ax[1,1].set_title("week4")
# เซตค่า title ของ figure
plt.suptitle("Temperature on December (Celcius)")
# ปรับการพล๊อตกราฟของ subplots ให้พอดีกับพื้นที่ของ figure
fig.tight_layout()
plt.show()