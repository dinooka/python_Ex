if __name__ == '__main__':
    N = int(input())

    list = []

    def insert(i, e):
        list.insert(i,e)
    def remove(e):
        list.remove(e)
    def append(e):
        list.append(e)
    def sort():
        list.sort()
    def pop():
        list.pop()
    def reverse():
        list.reverse()

    command = [None]*N
    for i in range(0,N):
        user_input = input()
        command[i] = user_input
        N = N-1
    
    command_len = len(command)
    text = [None]*command_len
    for i in range(0,command_len):
          
        text[i] = command[i].split()
        print(text)
    # for j in range(0,N):
    #     text = [None]*N
    #     text[j] = command[j].split()                

    #     if command[j].__contains__('append'):
    #         number1 = int(text[1])         
    #         append(number1)
    #         # N = N-1
    #     elif command[j].__contains__('insert'):
    #         number1 = int(text[1])
    #         number2 = int(text[2])         
    #         insert(number1,number2)
    #         # N = N-1
    #     elif command[j].__contains__('remove'):
    #         number1 = int(text[1])          
    #         remove(number1)
    #         # N = N-1
    #     elif command[j].__contains__('sort'):           
    #         sort()
    #         # N = N-1
    #     elif command[j].__contains__('reverse'):           
    #         reverse()
    #         # N = N-1
    #     elif command[j].__contains__('print'):           
    #         print(list)
    #         # N = N-1
        


            # insert(0,5)
            # insert(1,10)
            # insert(0,6)
            # print(list)
            # remove(6)
            # append(9)
            # append(1)
            # sort()
            # print(list)
            # pop()
            # reverse()
            # print(list)
            # N = N-1
