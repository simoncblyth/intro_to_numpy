#!/usr/bin/env python

import numpy as np
import sys


def header_metadata( path ):
    y = np.fromfile(path, np.uint8 )
    assert "".join(map(chr,y[:6])) == '\x93NUMPY'

    major,minor = y[6],y[7]
    assert major == 1 and minor == 0 

    # header length little-endian : byte with least significant bit sent first 
    lsb = y[8] ; msb = y[9] ; hlen = msb << 8 | lsb    

    assert (hlen + 10) % 16 == 0  

    meta = eval("".join(map(chr,y[10:10+hlen])).strip())
    meta['hlen'] = hlen 
    meta['major'] = major 
    meta['minor'] = minor 
    meta['path'] = path 

    return meta



def test_1():
    b = np.linspace(0,9,10, dtype=np.float32)
    path = "/tmp/b.npy" 
    np.save(path, b) 

    meta = header_metadata( path ) 
    print meta

    assert meta['shape'] == (10,)
    assert meta['descr'] == "<f4" 
    assert meta['fortran_order'] == False 



if __name__ == '__main__':

    path = sys.argv[1]
    meta = header_metadata( path ) 
    print meta

     


 



