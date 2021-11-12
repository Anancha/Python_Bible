import numpy as np

a = np.arange(24).reshape(4,3,2)

print("a = ")
print(a)
print("a[1:3:2,::2] = ")
print(a[1:3:2,::2])