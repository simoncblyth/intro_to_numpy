// gcc uifDemo.cc -lstdc++ && ./a.out -10 && rm ./a.out
#include <iostream>
#include <cassert>
#include "uif.h"

int main(int argc, char** argv)
{
    int value = argc > 1 ? atoi(argv[1]) : -10 ;  
    uif_t uif ; 
    uif.i = value ;  

    float a[3] = { 1.f, 1.f, 1.f } ; 
    a[1] = uif.f ; // plant int into float array

    uif_t uif2 ; 
    uif2.f = a[1] ; // float copy into 2nd union

    assert( uif2.i == value ) ; // recover int 

    std::cout 
        << " uif.u " << uif.u 
        << " uif.i " << uif.i 
        << " uif.f " << uif.f
        << " uif2.u " << uif2.u 
        << " uif2.i " << uif2.i 
        << " uif2.f " << uif2.f
        << std::endl ;  

    return 0 ; 
}

