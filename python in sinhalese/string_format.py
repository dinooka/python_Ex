# 4 string formatting types
# string concat, % type(like in the c lang.),format function, fstring

name = "Ann"
age = 33
sex = "female"
height = 171

# type 1 - string concat
msg1 = "Username is "+ name + " & the age is "+ str(age) +" & the gender is "+ sex

# type 2 - % type 
msg2 = "Username is %s & the age is %d & the gender is %s." % (name,age,sex)

# 3rd type - format function
# use '\' to split a statement in to 2 lines
msg3 =   "Username is {0} & the age is {1} & the gender +is {2}. \n{0} is a leftie."\
        .format(name,age,sex)
msg3 =   "Username is {} & the height is {:05d} & the gender is {}."\
        .format(name,height,sex)

# 4th type - fstring
msg4 =   f"Username is {name} & the height is {height:05d} & the gender is {sex}."
        
print(msg1)
print(msg2)
print(msg3)
print(msg4)