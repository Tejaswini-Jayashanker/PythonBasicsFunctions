""" This is a python program which serves as one approach to solve the following problem statement:
Write a function that uses a loop to print the Fibonacci series upto n terms called fibonacci_loop(n).

Explanation:

The Fibonacci Sequence is the series of numbers:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

The next number is found by adding up the two numbers before it:

    the 2 is found by adding the two numbers before it (1+1),
    the 3 is found by adding the two numbers before it (1+2),
    the 5 is (2+3),
    and so on!

"""
def fibonacci_loop(n_terms):

    first = 0
    second = 1
    
    print( first)
    print( second )
    
    for i in range( 2, n_terms ):
        next = first + second
        first = second
        second = next
        print(next)

number_terms = int( input("Enter the num of terms") )

if number_terms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   fibonacci_loop(number_terms)