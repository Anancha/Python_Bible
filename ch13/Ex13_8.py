class ParentClass:
    parent_msg = "This is parent class"

class ChildClass(ParentClass):
    child_msg = "This is child class"

child = ChildClass()
print(child.parent_msg)
print(child.child_msg)