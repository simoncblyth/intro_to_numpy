#!/usr/bin/env python
"""
http://louistiao.me/posts/numpy-mgrid-vs-meshgrid/

"""
import numpy as np

j, i = np.ogrid[0:10,0:10] 
N = len(j)*len(i)

g = np.zeros( [N, 3] )
g[:,0] = 
g[:,1] = 
g[:,2] = 0






import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter3D( g[:,0], g[:,1], g[:,2] )
plt.show()





