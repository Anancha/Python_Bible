import datetime

currentDT = datetime.datetime.now()
print ("วันนี้เป็นวันที่ ",currentDT.strftime("%Y/%m/%d"))
print ("ขณะนี้เป็นเวลา ",currentDT.strftime("%H:%M:%S"))
print ("Today is ",currentDT.strftime("%a, %b %d, %Y"))
