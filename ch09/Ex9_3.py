print("เกมส์ทายตัวเลข 1-10")
number = 0

while int(number) != 8 :
    number = input("ตัวเลขที่คุณทายคือเลขอะไร? : ")
    if(int(number) > 8) :
        print("ตัวเลขที่คุณทาย มากไป")
    elif(int(number) < 8) :
        print("ตัวเลขที่คุณทาย น้อยไป")
    else :
        print("คุณทายถูก ตัวเลขที่ถูกต้องคือ เลข 8")