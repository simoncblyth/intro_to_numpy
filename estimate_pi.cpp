//  clang++ -O3 -std=c++11 -stdlib=libc++ estimate_pi.cpp -o /tmp/estimate_pi_cpp 
// https://www.scratchapixel.com/lessons/mathematics-physics-for-computer-graphics/monte-carlo-methods-in-practice


#include <iostream> 
#include <iomanip> 
#include <random> 
#include <cmath>
 
int main(int argc, char **argv) 
{ 
    std::default_random_engine gen; 
    std::uniform_real_distribution<> uni ; 

    int square = (argc == 2) ? atoi(argv[1]) : 1024 ;
    int circle = 0; 

    for (int i = 0; i < square ; i++) 
    { 
        float x = uni(gen); 
        float y = uni(gen); 
        float l = sqrt(x * x + y * y); 
        if (l <= 1) circle++; 

        float estimate = 4.f*float(circle)/float(square) ;  
        float delta = estimate - M_PI ; 

        if( i % 100000 == 0 || i == N-1 )
        std::cout 
            << " square " << std::setw(10) << square 
            << " circle " << std::setw(10) << circle
            << " estimate_pi " << std::setw(10) << std::fixed << estimate
            << " delta " << std::setw(10) << std::fixed << delta
            << std::endl 
            ; 
    } 

 
    return 0; 
} 
