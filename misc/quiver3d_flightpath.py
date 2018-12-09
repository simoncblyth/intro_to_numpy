#!/usr/bin/env python
"""
https://matplotlib.org/gallery/mplot3d/quiver3d.html
"""
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np

plt.ion()
fig = plt.figure()
ax = fig.gca(projection='3d')


pz = 0.3 
phase0 = np.arccos(pz)
ta = np.linspace( 0, 2*np.pi , 32 )[:-1]    ## exclude the duplicate "seam" 
za = np.cos(ta+phase0)

m = np.argmin( np.abs(za[1:] - pz) ) + 1   ##  index closest to that pz value, going around 
t = ta[:m+1] 
n = len(t)


x = np.sin(t+phase0)
y = np.zeros(n)
z = np.cos(t+phase0)

# normal to circle, points up
u0 = x
v0 = y
w0 = z

# tangential
u1 = np.cos(t+phase0)
v1 = np.zeros(n)
w1 = -np.sin(t+phase0)

ax.quiver(x, y, z, u0, v0, w0, length=0.2, normalize=False, arrow_length_ratio=0.5 )
ax.quiver(x, y, z, u1, v1, w1, length=0.2, normalize=False, arrow_length_ratio=0.5 )


# take the last point and make an xy loop from it, around the z axis

r2 = np.abs(x[-1])


tb = np.linspace( 0, 2*np.pi, 32 )[:-1]
xb = r2*np.cos(tb)
yb = r2*np.sin(tb)
zb = z[-1]

_u0 = np.zeros(len(tb))
_v0 = np.zeros(len(tb))
_w0 = np.ones(len(tb))


_u1 = -r2*np.sin(tb)
_v1 = r2*np.cos(tb)
_w1 = np.zeros(len(tb))

ax.quiver( xb, yb, zb, _u0, _v0, _w0, length=0.2, normalize=False, arrow_length_ratio=0.5 )
ax.quiver( xb, yb, zb, _u1, _v1, _w1, length=0.2, normalize=False, arrow_length_ratio=0.5 )


















ax.set_xlim( -1, 1 )
ax.set_ylim( -1, 1 )
ax.set_zlim( -1, 1 )

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

plt.show()
