class Officer:
    def __init__(self, name, surname, sal):
        self.name = name
        self.surname = surname
        self.__salary = sal
    def display(self):
        print("\nName : ",self.name,self.surname)
        print("เงินเดือนเดิม : ",self.__salary)
    # Accessor Method
    def getSalary(self):
        print("เงินเดือนล่าสุด : ",self.__salary)
   # Mutator Method
    def setSalary(self, dept, sal):
        if dept!= "IT":
            if int(sal) > 50000:
                print("ไม่สามารถแก้ไขข้อมูลเงินเดือนใหม่ได้ ให้ใช้ข้อมูลเงินเดือนเดิม")
            else:
                self.__salary = sal
        else:
            self.__salary = sal

myname = input("กรุณากรอกชื่อ : ")
mysurname = input("กรุณากรอกนามสกุล : ")
mydept = input("กรุณากรอกแผนก : ")
oldsal = input("กรุณากรอกเงินเดือนเดิม : ")
newsal = input("กรุณากรอกเงินเดือนใหม่ : ")
ofc = Officer(myname,mysurname,oldsal)
ofc.display()
ofc.setSalary(mydept,newsal)
ofc.getSalary()