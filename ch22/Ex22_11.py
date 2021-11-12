import numpy as np

a = np.arange(100).reshape(5,10,2)
b = np.arange(5).reshape(5,1,1)
#a = np.arange(100).reshape(5,10,2)
#b = np.arange(10).reshape(5,1,2)
c = a*b
print(c)