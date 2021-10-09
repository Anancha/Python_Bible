import datetime

currentDT = datetime.datetime.now()
print(currentDT)
print("ปัจจุบัน คือ ปี ", currentDT.year)
print("ปัจจุบัน คือ เดือน " , currentDT.month)
print("ปัจจุบัน คือ วันที่ " , currentDT.day)
print("ตอนนี้เป็นเวลา " , currentDT.hour , "นาฬิกา",currentDT.minute , "นาที" , currentDT.second , "วินาที")
