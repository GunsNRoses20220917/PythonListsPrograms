# write a python program that will swap the elements in a list based on positions/indexes of values in list.

list1 = [1,2,3,4,5,6,7,8]

# index(list[1]) is 0
# index(list[2]) is 1
# index(list[3]) is 2
# index(list[4]) is 3
# index(list[5]) is 4
# index(list[6]) is 5
# index(list[7]) is 6
# index(list[8]) is 7

# the code should swap positions or indexes 4,7
# so at index 4 value should be 8 and at index 7 value should be 5

# swap the elements using comma assignment.
idx4 , idx7 = 4 , 7
list1[idx4] , list1[idx7] = list1[idx7] , list1[idx4]

print("after using comma assignment method, final list is:", list1)