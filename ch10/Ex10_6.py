def myclass(*std_name) :
  total_std = len(std_name)
  print("นักเรียนคนที่ 1 คือ ",std_name[0])
  print("นักเรียนคนสุดท้าย คือ ",std_name[total_std-1])

print("ห้อง 1/1")
myclass("นายดำ","นายแดง","นางสาวเขียว","นางสาวชมพู")
print("ห้อง 1/2")
myclass("นายกล้วย","นางสาวส้มเช้ง","นางสาวเชอรี่","นายองุ่น","นางสาวลำไย")

