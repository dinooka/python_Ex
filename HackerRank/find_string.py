def count_substring(string, sub_string):
    N = len(string)
    count = string.rfind(sub_string)
    # for i in range(0,N):
        

    return count

if __name__ == '__main__':
    my_string = input().strip()
    sub_string = input().strip()
    
    # count = count_substring(string, sub_string)
    count = my_string.find(sub_string)
    N1 = len(my_string)
    N2 = len(sub_string)
    print(count)