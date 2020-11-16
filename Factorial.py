'''
This is a Python Program to find factorial of a Number.
'''
def fact(num):

    if( number == 0):
        return "Not possible or Undefined"
    elif ( number < 0 ):
        return "Positive integer input only"
    
    fac_num = 1
    i = num
    while( i > 1):
        fac_num *= i
        i -= 1
    return int(fac_num)

number = float(input("Enter A Number"))
factorial = fact(number)
print(factorial)