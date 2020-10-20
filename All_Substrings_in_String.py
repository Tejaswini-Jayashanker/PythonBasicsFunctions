''' This is a python program which describes 1 solution to the given Problem statement:
Write a function to generate all substrings of a string and return it as a list of strings. L
et the function becalled generate_substrings(string). For example, generate_substrings("alchemy")returns ["a","al","alc","alch","alche","alchem","alchemy","l","lc",... etc]. 
Thereshould be no repititions in the list.
'''
# Function to print all sub strings
def generate_substrings( string ):
    
    str_len = len(string)
    subs_Str_list = []
    
    for i in range(str_len):
        for j in range( i , str_len):
            subs_Str_list.append( string[i : j+1 ] )
    return subs_Str_list
             
# Driver program to test above function
string_input = input("Enter a String")
str_list = generate_substrings(string_input)
print(str_list)