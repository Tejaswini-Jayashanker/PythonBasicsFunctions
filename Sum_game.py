'''This is a python code that describes one method as a solution to the given problem statement.
Write a function sum_game(value) that runs a loop that takes numbers as input from command line,
and exits only when the sum of the numbers so far reaches value. 
Make sure value is positive, but thenumbers which come from command line can be negative
'''
value = 20
def sum_game( value ):
    sum_res = 0
    #max_val = int(input("Enter Maximum value")) This can be used if user wants to enter the maximum limit
    while ( 1 ):
        num = int(input("Enter a number"))
        sum_res += abs(num)
        if( sum_res >= value):
            break
        else:
            pass

sum_game(value)