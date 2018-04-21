import matplotlib.pyplot as plt
import numpy as np

xlist = [1,12,15,29]
# xlist = [1,4,6,9,10]
ylist = [1,4,6,10]

plt.xlabel("Number of nodes killed (Q)")
plt.ylabel("Work Time (R) ")

plt.yticks(ylist)
plt.xticks(xlist)
plt.plot(xlist, ylist)
plt.title("For Dimension N=5 ")
plt.show()
# plt.savefig('temp.png')
