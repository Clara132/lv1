import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,3,1])
y= np.array([1,2,2,1,1])
plt.plot(x, y, 'r', linewidth=1, marker=".", markersize=8)
plt.axis([0,4,0,4])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Prvi zadatak')
plt.show()
