
#  python list can contain any data type
random_list = ["BMW",3.14,'c',28967462940,True,6]

for i in random_list:
    print(i,end=" ")

fruits = ["Apple","cherry","mango","Dragon fruit", "guava"] 

random_list.append("appended item")

print("\nAfter adding an item to list 1")
for i in random_list:
    print(i,end=" ")

print("\nAfter concatinating list 1 & list 2")
#  concatinate 2 lists
random_list.extend(fruits)
for i in random_list:
    print(i,end=" ")

print("\n\nAfter removing #6 from the random_list")
random_list.remove(6)
for i in random_list:
    print(i,end=" ")

print("\n\nIndex of the list")
count = fruits.index('guava')
print("Index of guava in the list = {}".format(count))

print(random_list)
print("\n\nremove Index #3 from the list")
random_list.pop(3)
print(random_list)

# check whether a specific element is in a list
is_var_in_list = "BMW" in random_list
# check whether a specific element is not in a list
# ex: "m001" is not any of the lists. so it will return true
is_var_not_in_list = "BMW" not in random_list
print(is_var_in_list)
print(is_var_not_in_list)


numbers = [23,2,76,899,1,"ttt"]
numbers.sort()
print(numbers)