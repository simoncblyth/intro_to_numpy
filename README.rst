Introduction To NumPy
=======================

Installing NumPy and other packages using conda
----------------------------------------------------

In addition to numpy some of the examples use
matplotlib and scipy for plotting and fitting. 

To install numpy and other python related packages 
I recommend the conda package manager which will
install python too.  This does not interfere with 
any preexisting python on your system.

* https://conda.io/docs/
* https://conda.io/docs/user-guide/install/index.html

After installing miniconda3, you can::

    conda install numpy ipython matplotlib     ## bare minimum 
    conda install scipy                        ## fitting + much more  
    conda install sympy                        ## symbolic maths  

All the most popular machine learning packages are also available
via conda. 


NumPy Documentation
----------------------

* http://www.numpy.org

See Also
----------

* https://simoncblyth.bitbucket.io/env/presentation/opticks_gpu_optical_photon_simulation_sep2018_qingdao.html

  Presention slides in html, with many NumPy examples.
  Once the images load  (it takes a while sometimes) the html provides a javascript 
  interface to navigate the slide pages, with menu at bottom right.

* https://simoncblyth.bitbucket.io/env/presentation/opticks_gpu_optical_photon_simulation_sep2018_qingdao.txt

  If your connection to bitbucket is slow, you can get the RST text sources of the slides at this URL

* https://bitbucket.org/simoncblyth/intro_to_cuda/

  Learning NumPy is ideal preparation for Learning CUDA...


Hello World Examples
----------------------

This repository contains a few very simple examples
of using NumPy.

* https://bitbucket.org/simoncblyth/intro_to_numpy/src/

Start by cloning the repository to a machine with NumPy installed::

    which hg    # Mercurial is required
    hg clone https://bitbucket.org/simoncblyth/intro_to_numpy


If you are planning to contribute and get write permission cloning from the ssh url is more convenient::

    hg clone ssh://hg@bitbucket.org/simoncblyth/intro_to_numpy



load/save NumPy arrays from C++
-----------------------------------

* https://github.com/simoncblyth/np


Highlighted Examples
-----------------------

recon.py
    * generate arrival times at coordinates on a sphere of a "disturbance" starting 
      within the sphere, assuming a normal distribution around geometric time

    * perform NLL minimization to find "disturbance" origin position parameters 
      from the arrival times at positions on the sphere 

    * positions, times and params are saved as npy files, for use by the recon
      extended example in 
      https://bitbucket.org/simoncblyth/intro_to_cuda/src/default/recon/
    
accept_reject_sampling.py
    demo technique with plot 

estimate_pi.py
    MC method estimate 

exponential_pdf_cdf.py
    use of matplotlib to make a simple plot 

header.py
    use np.fromfile to examine the NPY header of an array and extract 
    the metadata dict 

random_persist.py
    demonstrate random generation and persisting 

structured.py
    investigate numpy structured arrays, with composite dtype 

normal.py
    checking scipy.stats.norm 

dydx.py
    incomplete try at comparing numpy to python performance

python_vs_numpy_vs_cupy/ellipse_closest_approach_to_point.py
    compare python to numpy and cupy, in this example:
    
    * numpy is factor 10 faster than pure python
    * cupy is more than a factor 1000 faster than numpy
      (NVIDIA TITAN V) 



NumPy Introductions
--------------------

Python Ecosystem
~~~~~~~~~~~~~~~~~~

* http://www.scipy-lectures.org/index.html
* http://www.scipy-lectures.org/intro/intro.html


* http://www.scipy-lectures.org/intro/numpy/index.html


Slides
~~~~~~~~

* https://github.com/ContinuumIO/tutorials/blob/master/Intro_to_NumPy.pdf



