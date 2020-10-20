''' This is a python code which describes one method to solve the following problem statement:
Write a function check_substring(string1,string2) to check if string2 is a substring of string1.
For example "chem" is a substring of "alchemy" and "chemistry". It returns True or False.
'''
#Method - 1 using Find method.
def check_substring( string1, string2 ):
    if( string1.find(string2) == -1 ):
        return False
    else:
        return True

#Method - 2 using regular expressions from re module
'''
def check_substring( string1, string2 ):
    if re.search( string2, string1 ):
        return True
    else:
        return False
'''
#Method - 3 using Count method.
'''
def check_substring( string1, string2 ):
    if( string1.count(string2) > 0 ):
        return True
    else:
        return False
'''
str1 = input("Enter the String")
str2 = input("Enter the Substring")
flag_check = check_substring( str1, str2 )

if flag_check:
    print("Substring is a part of the String")
else:
    print("Substring is not a part of the string")