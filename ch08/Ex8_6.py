print("ราคาตั๋วเข้าชมพิพิธภัณฑ์ ผู้ใหญ่ 100 บาท เด็ก 50 บาท")

ticket_adult = input("ตั๋วผู้ใหญ่กี่ใบ? : ")
ticket_child = input("ตั๋วเด็กกี่ใบ? : ")

#คำนวณราคาตั๋วผู้ใหญ่
adult_price = int(ticket_adult)*100
#คำนวณราคาตั๋วเด็ก
child_price = int(ticket_child)*50

member = input("มีบัตรสมาชิกหรือไม่, พิมพ์ y (มี) หรือ n (ไม่มี) : ")

# กรณีเป็นสมาชิก และซื้อบัตรเด็ก
if member == "y" and int(ticket_child) != 0 :
    # ซื้อบัตร 10 ใบขึ้นไป จะได้ส่วนลด 50%
    if int(ticket_adult)+int(ticket_child) >= 10 :
        print("สำหรับสมาชิกที่ซื้อบัตรเด็ก และซื้อตั๋วตั้งแต่ 10 ใบขึ้นไป ลด 50% ทุกที่นั่ง")
        total_price = (adult_price+child_price) * 0.5
    # ซื้อบัตร 5 ใบขึ้นไป จะได้ส่วนลด 30%
    elif int(ticket_adult)+int(ticket_child) >= 5 :
        print("สำหรับสมาชิกที่ซื้อบัตรเด็ก และซื้อตั๋วตั้งแต่ 5 ใบขึ้นไป ลด 30% ทุกที่นั่งค่ะ")
        total_price = (adult_price+child_price) * 0.7
    # ซื้อบัตรไม่ถึง 5 ใบ จะได้ส่วนลด 20%
    else :
        print("สำหรับสมาชิกที่ซื้อบัตรเด็ก และซื้อตั๋วไม่ถึง 5 ใบ ลด 20% ทุกที่นั่งค่ะ")
        total_price = (adult_price+child_price) * 0.8
    print("ราคาตั๋วทั้งหมด " + str(total_price) + " บาท")
# กรณีเป็นสมาชิก และไม่ซื้อบัตรเด็ก จะได้ส่วนลด 10%
elif member == "y" and int(ticket_child) == 0 :
    print("สำหรับสมาชิกที่ไม่ซื้อบัตรเด็ก ลด 10% ทุกที่นั่งค่ะ")
    total_price = (adult_price+child_price) * 0.9
    print("ราคาตั๋วทั้งหมด " + str(total_price) + " บาท")
# กรณีไม่เป็นสมาชิก จะได้ส่วนลด 5%
elif member == "n" :
    print("ลูกค้าที่ไม่เป็นสมาชิก ลด 5% ทุกที่นั่งค่ะ")
    total_price = (adult_price+child_price) * 0.95
    print("ราคาตั๋วทั้งหมด " + str(total_price) + " บาท")
# กรณีระบุข้อมูลสมาชิกผิด (ไม่กรอก y หรือ n แต่กรอกค่าอื่น) จะคำนวณราคาตั๋วไม่ได้
else :
    print("ไม่สามารถระบุได้ว่าลูกค้าเป็นสมาชิกหรือไม่ จึงไม่สามารถคำนวณราคาตั๋วได้")