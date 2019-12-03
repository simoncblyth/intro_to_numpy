// gcc uifDemo.cc -lstdc++ && ./a.out -10
#include <iostream>
#include <cassert>
#include "uif.h"

int main(int argc, char** argv)
{
    int value = argc > 1 ? atoi(argv[1]) : -10 ;  

    float a[3] = { 1.f, 1.f, 1.f } ; 

    uif_t uif ; 
    uif.i = value ;  

    a[1] = uif.f ; // plant int in float array
    
    float b = a[1] ; 

    uif_t uif2 ; 
    uif2.f = b ;  


    std::cout 
        << " uif.u " << uif.u 
        << " uif.i " << uif.i 
        << " uif.f " << uif.f
        << " uif2.u " << uif2.u 
        << " uif2.i " << uif2.i 
        << " uif2.f " << uif2.f
 
        << std::endl ;  



    assert( uif2.i == value ) ; // recover int 

    return 0 ; 
}

