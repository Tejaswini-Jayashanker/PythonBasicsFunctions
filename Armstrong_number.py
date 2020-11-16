''' Assignment - 2:
Given an input, check if the number is an Armstrong number or not.
Output: Yes, is an Armstrong number.
		No, is not an Armstrong number.
'''

def check_armstrong_number( num ):
    temp_var = num
    sum_var = 0
    
    while ( temp_var > 0 ):
        digit_var = temp_var % 10
        sum_var += ( digit_var ** 3 )
        temp_var //= 10
    if( num == sum_var ):
        print("Yes! The number",num,"is an Armstrong Number")
    else:
        print("No! The number",num,"is not an Armstrong Number")
    return

number_inp = int(input("Enter a Number to check if it is an Armstrong Number"))
check_armstrong_number(number_inp)