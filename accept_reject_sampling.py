#!/usr/bin/env python
"""
::
 
   ipython -i accept_reject_sampling.py

"""

import numpy as np
import matplotlib.pyplot as plt 

pdf = lambda x:(3./8.)*(1+x**2)

if __name__ == '__main__':

    a = np.random.rand( 1000000,2 )    

    a[:,0] = a[:,0]*2. - 1.   #  [0,1] -> [-1,1]
    a[:,1] = a[:,1]*0.75      #  [0,1] -> [0,0.75]     pdf(0) = pdf(1) = 0.75

    w = np.where( a[:,1] < pdf(a[:,0]) )  # indices of accepted sample

    s = a[w][:,0]             # accepted sample


 
    sub = 5000    # size of smaller sample for scatter plots 
    wsub = np.where( a[:sub,1] < pdf(a[:sub,0]) )  # lower stats accept sample : for scatter plots 

    dom = np.linspace(-1,1,21)
    h,hx = np.histogram( s, bins=dom )        # histogram the accept sample
    assert np.all(hx == dom) 

    mx = (hx[:-1]+hx[1:])/2.                       # middle of bins

    x = np.linspace(-1,1,100)
    area = np.trapz( pdf(x), x) 
    print "check pdf normalization, with numerical integration: ", area

    fig = plt.figure()
    nx, ny = 2, 1

    plev = (pdf(mx[0])+pdf(mx[-1]))/2.             # pragmatic normalization 
    hlev = (h[0] + h[-1])/2.
    norm = plev/hlev

    ax0 = fig.add_subplot(ny,nx,0+1)
    ax0.plot(x, pdf(x), linewidth=4)
    ax0.scatter( a[:sub,0] , a[:sub,1], s=1, marker='o' ) 

    ax1 = fig.add_subplot(ny,nx,1+1)
    ax1.plot(x, pdf(x))
    ax1.scatter( a[wsub,0] , a[wsub,1], s=1, marker='o' ) 
    ax1.plot( mx, h*norm, drawstyle='steps-mid' )

    fig.show()


