''' This is a python code that describes one approach to solve the following Problem statement:
Write a function to print only odd numbers in the range(a,b). 
Write it two times - once with a for loop(print_odd_for(a,b)) 
and once with a while loop (print_odd_while(a,b)).
'''

def print_odd_for( a , b):
    for i in range( a, b +1 ):
        if( i%2 != 0 ):
            print(i)
        else:
            pass

def print_odd_while(a,b):
        i = a
        while( i < ( b + 1 ) ):
            if( i%2 != 0):
                print(i)
            else:
                pass
            i += 1

start = int(input("Enter the Start Point"))
end = int(input("Enter the end point" ))
print("Using For Loop")
print_odd_for(start,end)
print("Using While Loop")
print_odd_while(start,end)