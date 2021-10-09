class Employee:
    def __init__(self, emp_id, name, surname, dept, salary):
	                       # กำหนดค่าของ Properties
        self.emp_id = emp_id
        self.name = name
        self.surname = surname
        self.dept = dept
        self.salary = salary
# สร้างออบเจ็คของคลาส
myobj = Employee("001","สมศักดิ์","ใจกล้า","IT",36500)
print("รหัสพนักงาน : ",myobj.emp_id)
print("ชื่อนามสกุล : ",myobj.name,myobj.surname)
print("แผนก : ",myobj.dept)
print("เงินเดือน : ",myobj.salary)