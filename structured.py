#!/usr/bin/env python
"""

Explore how to parse NumPy structured array descr python dict 
outside of python/NumPy environment, eg from Opticks C++

Maybe after some simple replacements can use a json parser, 
to avoid having to write a python dict parser.


::

    In [84]: json.dumps(d)
    Out[84]: '{"shape": [3], "fortran_order": false, "descr": [["time", "<u8"], ["pos", [["x", "<f4"], ["y", "<f4"]]]]}'

    In [85]: s
    Out[85]: "{'descr': [('time', '<u8'), ('pos', [('x', '<f4'), ('y', '<f4')])], 'fortran_order': False, 'shape': (3,), }         \n"


    In [118]: dss
    Out[118]: 
    {u'descr': [[u'time', u'<u8'], [u'pos', [[u'x', u'<f4'], [u'y', u'<f4']]]],
     u'fortran_order': False,
     u'shape': [3]}

    In [119]: d
    Out[119]: 
    {'descr': [('time', '<u8'), ('pos', [('x', '<f4'), ('y', '<f4')])],
     'fortran_order': False,
     'shape': (3,)}



"""


import numpy as np
import json

spec = [  
           ('time',np.uint64),
           ('pos', [('x', np.float32), ('y', np.float32)])
        ]

dt = np.dtype(spec)


spec2 = [ ('i',np.uint32),  
          ('x',np.float32),
          ('y',np.float32) ]

dt2 = np.dtype(spec2)


x = np.array([(1, (0, 0.5)), 
              (2, (0, 10.3)),
              (3, (5.5, 1.1))], dtype=dt)


x2 = np.array( 
       [
         (1, 0, 0.5), 
         (2, 0, 10.3), 
         (3, 5.5, 1.1), 
        ], dtype=dt2 )



path = "/tmp/x.npy"

np.save(path, x )

y = np.fromfile(path, np.uint8 ) 
hdrlen = y[8]
s = "".join(map(chr,y[10:10+hdrlen])).strip()   ## reading NPY format header  

## simple replacements to make the python dict get past the json parser
ss = s.replace("(","[").replace(")","]").replace("'","\"").replace("False","false").replace("True","true").replace(",]","]").replace(", }"," }")
dss = json.loads(ss)

d = eval(s)

 
