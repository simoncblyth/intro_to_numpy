#!/usr/bin/env python 
"""
Toy Generate + Reconstruct
===========================

Reconstruct source position from times at sphere positions
with PDF model of a normal distribution around geometric time.

1. generate coordinates on a sphere
2. pick a truth position inside the sphere
3. mockup times at each sphere position based the distance from the truth position
4. save the sphere positions and times as NumPy arrays 
5. gratuitously find the closest sphere point to the truth point 
6. plot sphere positions in 3d, coloured according to the time
7. NLL minimization to reconstruct highest likelihood position for the times 
8. compare the reconstructed and truth positions and smearings  

The positions and times are persisted to /tmp/recon for GPU NLL
Minuit2 fitting with 

* https://bitbucket.org/simoncblyth/intro_to_cuda/src/default/fitRecon/fitRecon.cc

"""
import numpy as np
np.random.seed(0)  # reproducibility 

# generate n*n (x,y,z) coordinates on a sphere 
n = 50 
u,v = np.meshgrid( np.linspace(0,np.pi,n+2)[1:-1], np.linspace(0,2*np.pi,n+1)[:-1] )
uu = u.ravel()
vv = v.ravel()
sph = np.zeros( [len(uu), 3] )
sph[:,0] = np.sin(uu)*np.cos(vv)  
sph[:,1] = np.sin(uu)*np.sin(vv)  
sph[:,2] = np.cos(uu)  

R = 10 
sph *= R 

# pick a "truth" position inside the sphere 
parTru = np.array( [0,0,R/2, 1] ) 
parLab = np.array( ['x','y','z','s'], dtype="|S1" )

# distances from all the sphere coordinates to the true position 
d = np.sqrt(np.sum((sph - parTru[:3])**2, axis=1 ))

# mockup a time linear with the distance with a normal smearing      
t = d + parTru[3]*np.random.randn(len(d))     

# find the closest sphere point to the truth point 
closest = sph[np.argmin( np.sum( (sph - parTru[:3])**2 , axis=1 ) )] 
print("closest sph point to p ", closest)

# persist the sphere positions and time arrays to file
dir_ = "/tmp/recon"
import os
if not os.path.exists(dir_):os.makedirs(dir_)

print("saving to %s " % dir_ )
np.save(os.path.join(dir_, "t.npy"), t )
np.save(os.path.join(dir_, "sph.npy"), sph )
np.save(os.path.join(dir_, "parTru.npy"), parTru )
np.save(os.path.join(dir_, "parLab.npy"), parLab.view(np.uint8) )


# NLL (negative-log-likelihood) minimization to reconstruct position from the times
fit = True
if fit:
    from scipy.optimize import minimize
    import scipy.stats as stats

    parIni = np.array( [0,0,0,1] )  # initial parameter values

    t_model = lambda par:np.sqrt(np.sum((sph - par[:3])**2, axis=1 ))  

    ## Assumed PDF of time at each sphere position, normal around geometric time with some sigma.

    NLL = lambda par:-np.sum( stats.norm.logpdf(t, loc=t_model(par), scale=par[3] ))

    res = minimize(NLL, parIni, method='nelder-mead')
    parFit = res.x 

    print("NLL(parTru) ", NLL(parTru) )
    print("NLL(parIni) ", NLL(parIni) )
    print("NLL(parFit) ", NLL(parFit) )
    print("parTru", parTru)
    print("parIni", parIni)
    print("parFit", parFit)
    print("parFit-parTru", parFit-parTru)
pass









# plot the sphere positions, and give them a color based on the time
plot = False
if plot:
    import matplotlib.pyplot as plt 
    from mpl_toolkits.mplot3d import Axes3D
    plt.ion()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter3D( sph[:,0], sph[:,1], sph[:,2] , c=t )
    plt.show()
pass




