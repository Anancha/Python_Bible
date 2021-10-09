class OperatorOverloading:
    def __init__(self, a):
        self.a = a
  
    def __add__(self, other):
        return self.a + other.a
    
    def __gt__(self, other):
        if(self.a>other.a):
            return True
        else:
            return False
  
oo1 = OperatorOverloading(25)
oo2 = OperatorOverloading(35)
oo3 = oo1 + oo2
print("25+35 =",oo3)
if(oo1>oo2):
    print("Greater than")
else:
    print("Less than")