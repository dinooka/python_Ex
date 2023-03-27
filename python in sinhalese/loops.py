num = [1,2,3,4,5,9]

# for index,value in enumerate(num):
#     print(index,value)

# t = range(0,len(num))
# print(type(t))

# for i in t:
#     print(num[i],end=" ")

sum =0
for i in num:
    sum += i
print(f"Total = {sum}")
avg = sum/len(num)
print(f"Average = {avg}")

# find the min value

tip = [22,4,51,11,7,908,300]

min = tip[0]
max = tip[0]
N = len(tip) - 1
for i in range(0,len(tip)):
    if tip[i] < min:
        min = tip[i]
    if tip[i] > max:
        max = tip[i]

print(f"Min = {min}")
print(f"Max = {max}")





