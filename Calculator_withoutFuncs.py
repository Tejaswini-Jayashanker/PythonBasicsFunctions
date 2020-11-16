''' This is a program which describes 1 solution to the given problem statement as follows:
Take two input from the number and return sum, difference,product and Quotient of the input.
'''

num1 = int( input("Enter the First number") )
num2 = int( input("Enter the Second number") )

print("Sum of",num1,"and",num2,"is :",num1 + num2)
print("Difference of",num1,"and",num2,"is :",num1 - num2)
print("Product of",num1,"and",num2,"is :",num1 * num2)
if num2 == 0:
    print("Division Error")
else:
    print("Quotient of",num1,"and",num2,"is :",num1/num2)
    print("Remainder of",num1,"and",num2,"is :",num1%num2)
