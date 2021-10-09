class Officer:
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.__salary = salary
    def display(self):
        print("Call __salary from inside class")
        print("Officer Information")
        # เรียกใช้งานตัวแปร __salary จากภายในคลาส Officer
        print(self.name,ofc.surname,ofc.__salary)
        print("\n")

ofc = Officer("John", "Medola", 35000)
ofc.display()
print("Call __salary from outside class")
# เรียกใช้ตัวแปร __salary จากภายนอกคลาส Officer จะทำให้เกิดข้อผิดพลาดขึ้น
print(ofc.name,ofc.surname,": salary",ofc.__salary,"baht")