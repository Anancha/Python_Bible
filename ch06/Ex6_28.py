a = {"A":"Ant", "B":"Bird", "C":"Cat"}
b = {"A":"Aunt", "B": "Boy"}
c = {"A":1, "D":4}

a|=b
print(a)
print(b)
a|=c
print(a)
print(c)