def swap_case(s):
    
    # text = [None]*len(s)
    for i in s:
        if  i.islower():
            text= i.upper()
            if i.isupper():
                text = i.lower()
                return text
            # print(i.upper(),end="")

    # for j in s:
    #     if j.isupper():
    #         text = j.lower()
    #         return text
            # print(i.lower(),end="")
    
    # return text
if __name__ == '__main__':
    s = input()
    # swap_case(s)
    result = swap_case(s)
    print(result)


  