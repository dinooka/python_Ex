from lib2to3.refactor import MultiprocessingUnsupported

# names = ["kota", "maina",  "joka", "peniya", "kukula"]
# num = [1,2,3,4,5]
# #print(len(names))

# sum = 0
# mul = 1
# for i in num:
#     sum += i
#     mul *= i
# print(sum)
# print(MultiprocessingUnsupported)


# # range(0,len(num),1)



# marks = [24,76,88,12,65]


# for i in range(5):
#     for i in range(0,5,1):
#         print('*',end='')
#     print()
        

# tot=1
# for num in range(5):
#     pass
# print(tot)

# numbers = [3,2,5,7,8]
# count = 0
# for i in numbers:
#     count+=1
#     if i==1:
#         break
# else:
#     count=-1
# print(count)

# i = 0 > count = 1


# numbers = [3,2,5,7,8]
# count = 0
# for i in numbers:
#     count+=1
#     if i==5:
#         break
# else:
#     count=-1
# print(count)

# i = 0 > count = 1
# i = 1 > count = 2
# i = 2 > count = 3
# i = 3 > count = 4
# i = 4 > count = 5


# num = 5
# while (num !=0):			# 5,4, 3, 2, 1
#     print ("Hello World!") 
#     if (num == 2): 
#         break
#     num = num - 1 


# for r in range(5):
#     for c in range(10):
#         print('$',end='')
#     print()

# num = 5
# while (num !=0):
#     num = num - 1 
#     if (num == 2): 
#         continue
#     print ("Hello World!") 

# num = 5 -> "Hello World!"
# num = 4 -> "Hello World!"
# num = 3 -> "Hello World!"
# num = 1 -> "Hello World!"

# 2   **
#     **

# 5   *****
#     *****
#     *****
#     *****
#     *****

# val = int(input())
# for y in range(0,val):
#     for x in range (0, val):
#         print('*',end='')
#     print()

i = int(input())
j = 2                                         # fix the code (1) 
while (j <= (i/j)):
    if not(i%j):       
        print("not a prime")
        break                                    # fix the code (2)
    j = j + 1                                   # fix the code (3)
if (j > i/j): 
    print ("prime")


