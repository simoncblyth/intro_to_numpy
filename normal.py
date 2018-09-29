#!/usr/bin/env python
"""
Check can reproduce stats.norm.logpdf from basic operators
"""
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def normpdf(x, mu=0,sg=1):
    return np.exp(-(x-mu)*(x-mu)*0.5/(sg*sg))/np.sqrt(2*np.pi*sg*sg)

def normlogpdf(x, mu=0,sg=1):
    return -(x-mu)*(x-mu)*0.5/(sg*sg) - 0.5*np.log(2*np.pi*sg*sg)

if __name__ == '__main__':

    x = np.linspace(-5,5,100)
    loc = 10
    scale = 1.5 

    y0 = stats.norm.pdf(x,loc=loc, scale=scale) 
    y1 = normpdf(x,loc,scale)
    assert np.allclose( y0, y1 )

    z0 = stats.norm.logpdf(x,loc=loc, scale=scale)
    z1 = normlogpdf(x,loc,scale)
    assert np.allclose( z0, z1 )

    assert np.all( stats.norm.logpdf(x,loc,scale) == stats.norm(loc,scale).logpdf(x) )

   
    plt.ion()
    plt.plot( x, z0  )
    plt.plot( x, z1 )
    plt.show()


