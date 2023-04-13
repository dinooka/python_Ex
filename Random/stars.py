def print_square(n:int):
    for r in range(0,n):
        print("*"*n)   

def print_rectangle(r:int,c:int):
    for r in range(0,r):
        print("*"*c)
# *$$$$
# **$$$
# ***$$
# ****$
# *****

def triangle_type1(n:int):
    for r in range(0,n+1):
        for c in range(0,r+1):
            print("*"*c) # 
        print()

# $$$$*
# $$$**
# $$***
# $****
# *****

def triangle_type2(n:int):
    for r in range(n,0,-1):
        for c in range(0,(r+1)):
            print(" "*(r-1))
            print("*"*c)
        print()

# print_square(5)
# print_rectangle(4,7)
triangle_type2(3)