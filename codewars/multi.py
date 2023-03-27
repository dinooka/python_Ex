# This kata is about multiplying a given number by eight
# if it is an even number and by nine otherwise.

def mul(n):
    # n = int(input())

    return n*9 if (n%2 ==1) else (n*8)
    # if n%2 == 1:
    #     return n*9
    # else:
    #     return n*8
    
ans1 = mul(2)
ans2 = mul(1)
ans3 = mul(8)
ans4 = mul(4)
ans5 = mul(5)

print(ans1)
print(ans2)
print(ans3)
print(ans4)
print(ans5)

# test.assert_equals(simple_multiplication(2), 16)
# test.assert_equals(simple_multiplication(1), 9)
# test.assert_equals(simple_multiplication(8), 64)
# test.assert_equals(simple_multiplication(4), 32)
# # test.assert_equals(simple_multiplication(5), 45)