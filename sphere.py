#!/usr/bin/env python
import numpy as np

# generate coordinates on a sphere
# exclude poles and avoid duplication on phi seam
n = 10 
u,v = np.meshgrid( np.linspace(0,np.pi,n+2)[1:-1], np.linspace(0,2*np.pi,n+1)[:-1] )
uu = u.ravel()
vv = v.ravel()
assert len(uu) == len(vv) == n*n
nn = n*n

sph = np.zeros( [nn, 3] )
sph[:,0] = np.sin(uu)*np.cos(vv)  
sph[:,1] = np.sin(uu)*np.sin(vv)  
sph[:,2] = np.cos(uu)  

# plot the sphere positions
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter3D( sph[:,0], sph[:,1], sph[:,2]  )
plt.show()








