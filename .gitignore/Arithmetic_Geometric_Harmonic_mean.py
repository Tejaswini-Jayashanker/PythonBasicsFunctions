'''This File contains a Python code which serves as a solution to the following Problem Statement.
Write a function am_gm_hm(x,y) that takes as input two numbers and returns the Arithmetic Mean,
Geometric Mean and Harmonic mean of the two - in that order. What happens if one of the numbers is 0?
'''
import math as m

def am_gm_hm( x, y):
    arithmetic_mean = ( x + y ) / 2
    
    geometric_mean = m.sqrt( x * y)
    
    if( x == 0 or y == 0 ):
        print("Error! Cannot compute Harmonic Mean!")
        harmonic_mean = "ERROR"
    else:
        harmonic_mean = (arithmetic_mean ** ( -1) )
    return arithmetic_mean, geometric_mean, harmonic_mean

x, y = input("Enter two numbers").split( )
x = int(x)
y = int(y)
arit_mean, geo_mean, harm_mean = am_gm_hm(x,y)
print("The Arithmetic mean " + str(arit_mean) + " Geometric mean " + str(geo_mean) + " Harmonic mean " + str(harm_mean) )

