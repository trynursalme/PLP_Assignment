# Python Week 2 Assignment
my_list = []
# Append the following elements into my_list 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
# Insert the value 15 at the second position of my_list
my_list.insert(1,15)

#Extend my_list with the following elements 50,60,70
my_list.extend([50,60,70])
#Remove the last element from my_list
my_list.pop() # this will remove the last element 
# Sort my_list in ascending order
my_list.sort()
# Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print(f"The index of the value 30 in my_list is:{index_of_30}")