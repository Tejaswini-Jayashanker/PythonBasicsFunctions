''''This is a python code that describes one method as a solution to the given problem statement.
Write a function list_overlap(list1,list2) that takes two lists of integers as input, and returns a list of the common elements. Don't use sets for this.
'''
def list_overlap( list1, list2):
    common_list =[]
    for x in list1:
        for y in list2:
            if int(x ) == int(y):
                common_list.append(x)
    return common_list


# try block to handle the exception 
list_1 = input("Enter List - 1 elements").split( )  
list_2 = input("Enter List - 2 elements").split( )

res_list = list_overlap(list_1, list_2)
print("Common elements")
print(res_list)