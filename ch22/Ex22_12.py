import numpy as np

a = np.arange(50).reshape(5,5,2)
b = np.arange(10).reshape(5,2)
c = a*b
print(c)