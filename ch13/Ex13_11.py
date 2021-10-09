class GrandParentClass:
    def __init__(self, a):
        print("Call __init__ from GrandParentClass")
        self.a = a
        print("a = ",self.a)

class ParentClass(GrandParentClass): 
    def __init__(self, a, b):
        super().__init__(a)
        print("Call __init__ from ParentClass")
        self.b = b
        print("b = ",self.b)

class ChildClass(ParentClass):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        print("Call __init__ from ChildClass")
        self.c = c
        print("c = ",self.c)

child = ChildClass(1, 2, 3)
print("a b c = ",child.a,child.b,child.c)