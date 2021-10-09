f = open("student_record2.txt","r",encoding="UTF-8")
print("อ่านข้อมูลด้วยเมธอด read()")
std_data = f.read()
print(std_data)

f.seek(0)
print("\nอ่านข้อมูลด้วยเมธอด readline()")
std_data = f.readline()
print(std_data)

print("\nอ่านข้อมูลด้วยเมธอด readlines()")
f.seek(0)
std_data = f.readlines()
print(std_data)

f.close()