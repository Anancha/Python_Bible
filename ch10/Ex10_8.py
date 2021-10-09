def rectangle_area(width,length) :
  return width * length

w = int(input("กรุณากรอกความกว้าง : "))
h = int(input("กรุณากรอกความยาว : "))
area = rectangle_area(w,h)

print("พื้นที่สี่เหลี่ยมผืนผ้า คือ ",area)
