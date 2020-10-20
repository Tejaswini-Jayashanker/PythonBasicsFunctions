""" This is a python program which serves as one approach to solve the following problem statement:
Write a function that uses recursion to calculate the nth term of the Fibonacci series called fibonacci(n). (Google fibonacci series if you don't know it.)

Explanation:

The Fibonacci Sequence is the series of numbers:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

The next number is found by adding up the two numbers before it:

    the 2 is found by adding the two numbers before it (1+1),
    the 3 is found by adding the two numbers before it (1+2),
    the 5 is (2+3),
    and so on!

"""


def fibonacci(num):
   if num <= 1:
       return num
   else:
       return(fibonacci(num-1) + fibonacci(num-2))

number_terms = int( input("Enter the num of terms") )

if number_terms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(number_terms):
       print(fibonacci(i))