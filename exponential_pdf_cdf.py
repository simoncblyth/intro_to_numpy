#!/usr/bin/env python
"""

ipython -i exponential_pdf_cdf.py

::

   cdf(x) = 1 - exp(-x/mu) 


* https://www.eg.bucknell.edu/~xmeng/Course/CS6337/Note/master/node50.html


"""
import numpy as np


t = np.linspace( 0, 10, 100 )

a = 2. 
A = 1./a

pdf = lambda t:A*np.exp(-t*A) 

cdf = lambda t:1.-np.exp(-t*A) 


import matplotlib.pyplot as plt 
fig = plt.figure()

ax = fig.add_subplot(1,2,1)
#ax.set_xlabel("PDF(x; a:%s ) = (1/a)*exp(-x/a) " % a)
ax.plot( t, pdf(t) )
plt.title(" PDF(x) =  (1/a)exp(-x/a)     a = 2  ")

ax = fig.add_subplot(1,2,2)
#ax.set_xlabel("CDF(x; a:%s) = 1 - exp(-x/a) " % a )
ax.plot( t, cdf(t) )
plt.title(" CDF(x) = 1 - exp(-x/a) ")

plt.annotate( " CDF(x) = u  ", xy=(3,0.5) )
plt.annotate( " X = -a ln(1 - u) ", xy=(3,0.4) )


fig.show()







