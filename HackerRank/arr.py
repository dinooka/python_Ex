import numpy

def arrays(arr):
    # complete this function
    # use numpy.array

    for i in range((len(arr-1)),0,-1):
        return arr[i]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)