class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

class Student(Person):
    def __init__(self, name, surname, age, grade):
        super().__init__(name, surname, age)
        self.grade = grade
        
s = Student("สมศรี", "สดใส", "16", "3.58")
print(s.name, s.surname, "อายุ", s.age, "ปี เกรด", s.grade)