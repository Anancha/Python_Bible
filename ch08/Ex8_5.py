score = input("กรุณากรอกคะแนน : ")
if int(score) >= 80 :
    print("คุณเก่งมากๆเลย")
    print("คุณได้เกรด A")
elif int(score) >= 70 :
    print("คุณได้เกรด B")
elif int(score) >= 60 :
    print("คุณได้เกรด C")
elif int(score) >= 50 :
    print("คุณได้เกรด D")
else :
    print("คุณได้เกรด F")
    print("พยายามใหม่นะ")
print("แล้วพบกันใหม่เทอมหน้า")