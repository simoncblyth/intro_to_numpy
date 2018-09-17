#!/usr/bin/env python
"""

::
 
   ipython -i estimate_pi.py 

"""
from __future__ import division
import numpy as np

if __name__ == '__main__':

    a = np.random.rand( 1000000,2 )    

    a[:,0] = a[:,0]*2. - 1. 
    a[:,1] = a[:,1]*2. - 1. 


    mask = np.sum(a*a,1) < 1
    w = np.where(mask) 
    epi = 4*len(w[0])/len(a) 

    label = " estimate_pi 4*%d/%d = %10.5f  (%10.5f) " % (len(w[0]), len(a), epi, epi-np.pi ) 
    print label 


    imask = np.logical_not( mask )
    iw = np.where(imask) 




    import matplotlib.pyplot as plt 
    fig = plt.figure()

    plt.title(label)
    ax = fig.add_subplot(1,1,1)

    s = 0.01
    ax.scatter( a[w][:,0], a[w][:,1] , s=s)
    ax.scatter( a[iw][:,0], a[iw][:,1] , s=s )

    fig.show()



