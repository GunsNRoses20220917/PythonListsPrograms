# write a Python List program that will interchange First and Last element in a List.

# method 1: to swap the first with last and vice versa
list1 = [1,2,3,4,5,6,7,8,'Life']
# print(list1)

print(list1[0])
print(list1[-1])

list1[0],list1[-1] = list1[-1],list1[0]

print(list1)