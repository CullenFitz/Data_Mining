from numpy import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

fig = plt.figure()
ax = plt.axes(projection='3d')



mu = [0,0,0]
mu = np.transpose(mu)

cov = [[1,1,1], [1,3,3], [1,3,6]]

v, w = np.linalg.eig(cov)

dist = random.multivariate_normal(mu, cov, size=1000)

xdata = []
ydata = []
zdata = []
for i in dist:
    xdata.append(i[0])
    ydata.append(i[1])
    zdata.append(i[2])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens')

plt.show()

