import numpy as np

a = np.arange(25).reshape(1,5,5)
b = np.arange(5).reshape(5,1,1)
c = a*b
print(c)