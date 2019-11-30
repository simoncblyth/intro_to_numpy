#!/usr/bin/env python
import numpy as np, scipy.stats as st, scipy.optimize as so
np.random.seed(0)  # reproducibility

n = 50     # generate n*n (x,y,z) coordinates on a sphere 
u,v = np.meshgrid( np.linspace(0,np.pi,n+2)[1:-1], np.linspace(0,2*np.pi,n+1)[:-1] )
uu = u.ravel()
vv = v.ravel()
sph = np.zeros( [len(uu), 3] ) 
sph[:,0] = np.sin(uu)*np.cos(vv)  
sph[:,1] = np.sin(uu)*np.sin(vv)  
sph[:,2] = np.cos(uu)  
R = 10 
sph *= R  

parTru = np.array( [0,0,R/2, 1] )  # pick "true" position 

# distances from all the sphere coordinates to the "true" position 
d = np.sqrt(np.sum((sph - parTru[:3])**2, axis=1 ))

# mockup a time linear with the distance with a normal smearing     
t = d + parTru[3]*np.random.randn(len(d))    

parIni = np.array( [0,0,0,1] )  # initial parameter values
t_model = lambda par:np.sqrt(np.sum((sph - par[:3])**2, axis=1 ))

# Assumed PDF of time at each sphere position, normal around geometric time with some sigma.
NLL = lambda par:-np.sum( st.norm.logpdf(t, loc=t_model(par), scale=par[3] ))

parFit = so.minimize(NLL, parIni, method='nelder-mead').x
print(parFit)

