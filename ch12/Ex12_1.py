f1 = open("student_record.txt","w",encoding="UTF-8")
f1.write("ข้อมูลนักเรียนอนุบาล 1/1")
f1.write("1. น้องดีน่า")
f1.write("2. น้องต้นไม้")
f1.write("3. น้องดีใจ")
f1.write("4. น้องเมียวจัง")
f1.write("5. น้องรักดี")

f2 = open("student_record2.txt","w",encoding="UTF-8")
f2.writelines(["ข้อมูลนักเรียนอนุบาล 1/2" , "\n1. น้อง A" , "\n2. น้อง B" , "\n3. น้อง C"])

f2.close()
f1.close()