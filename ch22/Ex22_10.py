import numpy as np

a = np.arange(50).reshape(5,10)
b = np.arange(5).reshape(5,1)
c = a*b
print(c)