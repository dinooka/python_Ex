def is_even(n):
    return "E" if (n % 2 == 0) else "O"

# lambda for above function
eve = lambda n : "E" if (n % 2 == 0) else "O"

a = [11,22,36,44,55,63,77,81]
b = []

# list comp. is speed coz v r using less variables
b = [{v :eve(v)} for i,v in enumerate(a) if i % 2 ==0]

# b.append(100)

# print(f"a = {a}")
# print(f"b = {b}")

arr1 = [11,22,33,44]
arr2 = [1,2,3,4]

arr3 = [(arr1[i] + arr2[j]) for i in range(0,len(arr1))
        for j in range(0,len(arr2))]

print(len(arr3))
print(arr3)
