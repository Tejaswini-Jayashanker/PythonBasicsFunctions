''' This is a pyhton program that solves the following Problem Statement:
Triangle inequality states that for the sum of any two sides of a triangle is greater than the third side.
Write a function check_triangle_inequality(a,b,c) that returns False if some combination of sidesviolates the triangle inequality (Hint: there are 3 scenarios) and True otherwise.
'''

def check_triangle_inequality( a, b, c):
    if( ( ( a + b) > c ) and ( ( b + c ) > a ) and  ( ( c + a ) > b ) ):
        return True;
    else:
        return False;

side_1, side_2, side_3 = input("Enter the dimensions of three sides of a triangle").split( )

side_1 = int( side_1 )
side_2 = int( side_2 )
side_3 = int( side_3 )

flag_check = check_triangle_inequality( side_1, side_2, side_3 )

if( flag_check ):
    print("Triangle Inequality Check passed")
else:
    print("Triangle Inequality fails")
        
