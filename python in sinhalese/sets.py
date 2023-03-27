
# consider a set in maths.
prince = {"Namal","Baby","Namal",1,1}

prince.add(1)
prince.add("namal")
# if we want to get distinct values from a collection we can use set
print(prince)

prince.remove(1)
print(prince)

# google hash function, how has function use in sets & dictionary
# cant access sets using index

king = {'Mahinda','Charles','Chin Hu'}

# add 2 sets
z = prince.union(king)
print(z)

# add 2 sets using pipe 
q = prince | king
print(q)


# sets substraction
first_set = {1,2,33,"hello"}
second_set = {11,22,33,"hello"}

sub_set = first_set - second_set
print("fist set - second set = {}" .format(sub_set))
sub_set = second_set - first_set
print("fist set - second set = {}" .format(sub_set))


print(1 in first_set)
print(4 not in first_set)