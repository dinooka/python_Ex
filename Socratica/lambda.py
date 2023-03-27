# calc 3x+1
cal = lambda x : 3 * x + 1
print(cal(3))

# concat fname & lname
fullname = lambda fname,lname : fname.title() + ' ' + lname.title()
print(fullname('mahinda','mahattaya'))

# sort a list
names = ['Joseph Chaminda Vass','Sanath Teran Jayasuriya',
         'Marvan Athapattu','Kumar Chokshananda Sangakkara',
         'Kusal Gimhan Mendis','Dimuth Karunarathne']

names.sort(key=lambda names:names.split(' ')[-1])
print(names)

# ax**2 + b*x + c
fx = lambda a,b,c,x : (a*x**2 + b*x +c)
# 2 + 3 + 5
# print(fx(2,3,5,1))

def build_quadratic_function(a,b,c):
    return lambda x : a*x**2 + b*x + c

print(build_quadratic_function(2,3,5)(1))