#!/usr/bin/env python
"""
ipython -i t.py::


    In [6]: np.average(t[N/2+1:])
    Out[6]: 0.0005220174789428711

    In [7]: np.average(t[1:N/2])
    Out[7]: 0.6991509795188904

    In [8]: np.average(t[1:N/2])/np.average(t[N/2+1:])
    Out[8]: 1339.324845855218

"""

import numpy as np, cupy as cp


def timed(func):
    def wrapper(*args, **kwa):
        import timeit
        t0 = timeit.default_timer()
        r = func(*args,**kwa)
        t1 = timeit.default_timer()
        return r, t1-t0
    return wrapper


def ellipse_closest_approach_to_point( xp, ex, ez, _c, N ):
    """ex, ez: ellipse semi-axes, c: coordinates of point in ellipse frame"""
    c = xp.asarray( _c )  ; assert c.shape == (2,)

    t = xp.linspace( 0, 2*xp.pi, N )      # t: array of 1M angles [0,2pi] 
    e = xp.zeros( [len(t), 2] )
    e[:,0] = ex*xp.cos(t)
    e[:,1] = ez*xp.sin(t)                       # e: 1M parametric [x,z] points on the ellipse 

    return  e[xp.sum((e-c)**2, axis=1).argmin()]    # point on ellipse closest to c 


def pure_python_ellipse_closest_approach_to_point_DO_NOT_DO_THIS( ex, ez, _c, N):
    """
    DEMONSTRATION OF WHAT YOU SHOULD NOT DO IN PYTHON
    (THIS STYLE WOULD BE FINE IN C/C++, BUT NOT PYTHON) 
    """
    import math
    ddmn = None
    tmn = None

    for i in range(N):
        t = i*np.pi*2./(N-1)
        x,y = ex*math.cos(t),ey*math.sin(t)
        dx,dy = x-_c[0],y-_c[1]
        dd = dx*dx+dy*dy   

        if ddmn is None:
            ddmn = dd
            tmn = t 

        if dd < ddmn:
            ddmn = dd
            tmn = t 
        pass
    pass
    return ex*math.cos(tmn),ey*math.sin(tmn)


if __name__ == '__main__':

    N = 10000000
    M = 20 

    ex,ey = 10,20
    c = [100,100]

    r = {}
    t = np.zeros(M)

    for i in range(M):
        if i == 0:
            r[i],t[i] = timed(pure_python_ellipse_closest_approach_to_point_DO_NOT_DO_THIS)(ex,ey,c,N)
        else:
            r[i],t[i] = timed(ellipse_closest_approach_to_point)( np if i < M/2 else cp, ex,ey,c, N )
        pass
    pass
    for k in r.keys():
        if k == M/2: print("")
        print(k, r[k], t[k])
    pass







