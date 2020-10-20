''' This is a python program which describes 1 method of solving the below problem statement:
You already know how to calculate factorials from the lecture. 
Use that function (or better write it again by yourself) to compute the value of sin(x) according to the Taylor formula upto k terms. 
Thus your functionshould be calculate_sin(x,k). 
The Taylor formula for sin(x) is as follows-
sin(x) = x - x^3/3! + x^5/5! - x^7/7! + x^9/9! ...
'''

def factorial_number( num ):
    fac_num = 1
    i = num
    while( i > 1):
        fac_num *= i
        i -= 1
    return fac_num
    
def compute_sin_x( num, no_terms ):
    sinx_res = 0

    for itr in range(no_terms):
        sinx_res += (num**(itr) )/factorial_number(itr)
    return sinx_res
    

number = int(input("Enter a number"))
number_terms = int( input( "Enter the number of terms upto which Sin(x) should be computed") )
sin_x = compute_sin_x(number, number_terms)
print("The Sin_X is:" + str(sin_x) )