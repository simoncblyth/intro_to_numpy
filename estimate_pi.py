#!/usr/bin/env python
"""

::
 
   ipython -i estimate_pi.py 

"""

import numpy as np


def estimate_pi( a ):
    num_square = len(a)
    num_circle = np.count_nonzero( np.sum(a*a, 1) < 1 ) 
    estimate = 4.*float(num_circle)/float(num_square)
    print "square %10d , circle %10d  estimate %10.6f  delta %10.6f " % ( num_square, num_circle, estimate, estimate - np.pi )


if __name__ == '__main__':

    n, M = 40, 1000000
    a = np.random.rand( n*M,2 )    

    for n in range(n):   
        estimate_pi(a[:(n+1)*M])
    pass


#import matplotlib.pyplot as plt 
#fig = plt.figure()
#ax = fig.add_subplot(1,1,1)
#ax.scatter( a[:,0], a[:,1] )
#fig.show()



