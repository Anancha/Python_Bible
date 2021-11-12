import matplotlib.pyplot as plt

x = [1,2,3]
y = [1,4,9]
plt.figure(figsize=[4,6],dpi=60)
plt.plot(x,y)
plt.savefig("LineGraphs03.png")
plt.show()