try :
    number1 = int(input("กรุณากรอกตัวเลขที่ 1 : "))
    number2 = int(input("กรุณากรอกตัวเลขที่ 2 : "))
    print(number1/number2)
except ValueError :
    print("คุณกรอกข้อมูลผิด กรุณากรอกข้อมูลตัวเลข")
except ZeroDivisionError :
    print("ไม่สามารถหารตัวเลขด้วยศูนย์ได้")
finally :
    print("จบการทำงานของโปรแกรม")