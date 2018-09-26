#!/usr/bin/env python


import numpy as np

def pyloop(N, f):
    x0 = float(0)
    y0 = f(x0)
    dydx = []
    for i in range(1,N+1):
        x = float(i)
        y = f(x) 
        dydx_ = (y - y0)/(x - x0)
        x0,y0 = x,y
        dydx.append(dydx_)
    pass
    return dydx 

def npvec(N, f):
    x = np.linspace(0, float(N), N+1 )
    y = f(x)
    dydx = (y[1:] - y[:-1])/(x[1:]-x[:-1])
    return dydx 
    

if __name__ == '__main__':

    
    N = 1000000
    func = lambda _:_**2 

    a0 = pyloop(N, func)
    a1 = npvec(N, func )

    assert np.all( np.array(a0) == a1 )

    #r0 = %timeit -o pyloop(N,func)
    #r1 = %timeit -o npvec(N,func)

 
 



