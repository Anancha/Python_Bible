class Animal:
    def __init__(self, type, color):
        self.type = type
        self.color = color
        print("ฉันเป็น ",self.type,"สี",self.color)
    def yell(self):
        print("ฉันสามารถส่งเสียงร้องได้\n")

class Rat(Animal):
    pass

class Dog(Animal):
    def yell(self):
        print("ฉันร้องโฮ่ง โฮ่ง\n")
    

class Cat(Animal):
    def yell(self):
        print("ฉันร้องเหมียว เหมียว\n")

r = Rat("หนู","เทา")
r.yell()
d = Dog("สุนัข","ขาว")
d.yell()
c = Cat("แมว","ดำ")
c.yell()