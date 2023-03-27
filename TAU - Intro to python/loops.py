

names = ["ann", "tim","pamela", "james"]

def loop():
    for i in names:
        print(i)


# for i in range(start,end, increment):

# for i in range(1,10,2):
#     print(i)
# # start(inclusive), end(exclusive)

# for i in range(1,10):
#     print(i)

# if increment isn't specified default value is 1
# If start is not specified, it defaults to 0

# *
# **
# ***
# ****
# *****
'''
c=2
for i in range(1,6,1):
    for j in range(1,c,1):
        print("*", end="")
        c += 1
    # print()
'''

# (1,2,1)   *
# (1,3,1)   **
# (1,4,1)   ***


temp = 40

# while temp>33:
    # print("The water is {} degrees".format(temp))
    # temp -=1
    # break

for i in range(1,11):
    if i == 7:
        print("We are skipping number 7")
        continue
    print("This is the number {}".format(i))  