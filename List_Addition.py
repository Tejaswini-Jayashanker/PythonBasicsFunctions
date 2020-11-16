#Input 2 lists and add the elements. Also concatenate the lists.

list_1 = list(input ("Enter the First list elements") )
list_2 = list(input ("Enter the Second list elements") )
res_list = []
list_1_len = len(list_1)
list_2_len = len(list_2)

for i in range(list_1_len):
    res_list.append(list_1[i] + list_2[i])

print("The Added values are:",res_list)
print("The Concatenated lists are : ", list_1 + list_2 )
