class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def display(self):
        print(self.name, self.surname, "อายุ", self.age, "ปี")

class Student(Person):
    pass
        
p = Person("สมศักดิ์", "ใจกล้า", "15")
p.display()
s = Student("สมศรี", "สดใส", "16")
s.display()