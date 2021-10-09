class Employee:
    def __init__(self, emp_id, name, surname, dept, salary):
        self.emp_id = emp_id
        self.name = name
        self.surname = surname
        self.dept = dept
        self.salary = salary
    def mymethod(self):
        if(self.dept == "IT"):
            print("แผนก : Information Technology")
        else :
            print("แผนก : ", self.dept)

myobj = Employee("001","สมศักดิ์","ใจกล้า","IT",36500)
print("ชื่อนามสกุล : ",myobj.name,myobj.surname)
myobj.mymethod()
print("\n")
myobj2 = Employee("002","สมศรี","สวยไสว","HR",25000)
print("ชื่อนามสกุล : ",myobj.name,myobj.surname)
myobj2.mymethod()