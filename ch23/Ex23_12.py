import pandas as pd
import numpy as np

# สร้าง ndarray ของ Numpy
array = np.array([["ด.ช.สมชาย", "ใสดี", 3.83], ["ด.ญ.สมใจ", "เรียนดี", 2.82],
                  ["ด.ญ.แก้มใส", "วินียดี", 3.50], ["ด.ช.สมเกียรติ", "รักไทย", 2.95],
                  ["ด.ญ.สมหญิง", "ถิ่นไทย", 2.68]])

# สร้างลิสต์ของ index
index_values = ["001", "002", "003", "004", "005"]

# สร้างลิสต์ของชื่อคอลัมน์
column_values = ["ชื่อ", "นามสกุล", "เกรด"]

df = pd.DataFrame(data=array, index=index_values, columns=column_values)
print(df) 