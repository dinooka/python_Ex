def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    # print(x,end=" ")
    my_list = [None]*n
    sum =0
    while(n>0):
        sum +=x
        n -=1
        my_list = sum
        return my_list
    #     print(sum,end=" ")
    # print()


list1 = count_by(1, 5)
print(list1)
# count_by(2, 5)
# count_by(3, 5)
# count_by(50, 5)
# count_by(100, 5)
#         test.assert_equals(count_by(1, 5), [1, 2, 3, 4, 5])
#         test.assert_equals(count_by(2, 5), [2, 4, 6, 8, 10])
#         test.assert_equals(count_by(2, 5), [3, 6, 9, 12, 15])
#         test.assert_equals(count_by(50, 5), [50, 100, 150, 200, 250])
#         test.assert_equals(count_by(100, 5), [100, 200, 300, 400, 500])