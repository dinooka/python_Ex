num = [1,2,3,4,5]

sum = 0
# list comprehension
[sum := (sum+i)  for i in num]
# print(type(sum))
# print(sum)

mul = 1
[mul :=mul*i for i in num]
# print("multiplication = ",mul)

# find the a value is > avg
marks = [34,77,88,51,48]

n= [i for i in marks if i>50]
print("Above average numbers : ",end='')
for i in n:
    print(i ,end=' ')


