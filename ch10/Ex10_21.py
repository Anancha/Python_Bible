from zoneinfo import ZoneInfo
from datetime import datetime

dt1 = datetime(2000, 1, 25, 12, tzinfo=ZoneInfo("Asia/Bangkok"))
print("วันเวลาปัจจุบันของกรุงเทพฯ คือ ",dt1)

dt2 = datetime(2000, 1, 25, 12, tzinfo=ZoneInfo("Europe/London"))
print("วันเวลาปัจจุบันของลอนดอน คือ ",dt2)

print("เทียบวันเวลา : ถ้าวันเวลากรุงเทพฯ คือ ", dt1 , "แล้ววันเวลาปัจจุบันของลอนดอน คือ " , dt1.astimezone(ZoneInfo("Europe/London")))

print("เทียบวันเวลา : ถ้าวันเวลาลอนดอน คือ ", dt2 , "แล้ววันเวลาปัจจุบันของกรุงเทพฯ คือ " , dt2.astimezone(ZoneInfo("Asia/Bangkok")))