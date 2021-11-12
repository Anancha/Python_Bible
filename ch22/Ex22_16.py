import numpy as np

a = np.arange(20).reshape(4,5)
b = np.arange(20).reshape(10,2)
c = a*b
print(c)