'''This is a python code that describes one approach to solve the below problem statement:
Write a function mean_calculator() to take two floats as input from command line and print the AM,GM,HM of those numbers.
'''
def mean_calculator( fl_num_1, fl_num_2):
    
    arithmetic_mean = (fl_num_1 + fl_num_2 ) / 2
    
    geometric_mean = (fl_num_1 * fl_num_2)**0.5
    
    if( fl_num_1 == 0.0 or fl_num_2 == 0.0):
        harmonic_mean = "ERROR"
    else:
        harmonic_mean = 1/(arithmetic_mean)
    return arithmetic_mean, geometric_mean, harmonic_mean

fl_number_1 = float( input( "Enter the first Number" ) )
fl_number_2 = float( input( "Enter the second Number" ) )

AM, GM, HM = mean_calculator( fl_number_1, fl_number_2 )
print("The AM is : " + str(AM))
print("The GM is : " + str(GM))
print("The HM is : " + str(HM)) 