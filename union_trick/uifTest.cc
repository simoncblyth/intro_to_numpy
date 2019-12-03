// gcc uifTest.cc -lstdc++ && ./a.out -10
#include <iostream>
#include <cassert>
#include <cmath>
#include "uif.h"

int main(int argc, char** argv)
{
    uif_t uif ; 
    uif.i = argc > 1 ? atoi(argv[1]) : 1 ;  

    for(int i=0 ; i < 3 ; i++) // check u,i,f 
    {
        uif_t chk ; 
        switch(i)
        {
            case 0: chk.u = uif.u  ;; 
            case 1: chk.i = uif.i  ;; 
            case 2: chk.f = uif.f  ;; 
        } 

        if(std::isnan(uif.f)) assert(std::isnan(chk.f))
        else assert( chk.f == uif.f ) ; 
        assert( chk.u == uif.u ) ; 
        assert( chk.i == uif.i ) ; 

        std::cout 
           << " i " << i  << std::endl  
           << " uif.u " << uif.u  
           << " uif.i " << uif.i  
           << " uif.f " << uif.f << std::endl 
           << " chk.u " << chk.u  
           << " chk.i " << chk.i  
           << " chk.f " << chk.f << std::endl 
           ; 
    }
    return 0 ; 
}

