try :
   number_dict = {
       1 : "one",
       2 : "two",
       3 : "three"
   }
   number_list = [1, 2, 3]
   print(number_dict[6])
   print(number_list[6])
except IndexError :
    print("คุณกำหนดตำแหน่งของข้อมูลผิดพลาด")
except KeyError :
    print("คุณกำหนดค่าคีย์ผิดพลาด ไม่มีคีย์ตามที่ระบุ")