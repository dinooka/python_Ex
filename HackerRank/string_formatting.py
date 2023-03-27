
def print_formatted(number):
    for i in range(1,number+1):
        # print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
        # print('{0:2d}'.format(i),end=" ")
        
        oc = (oct(i)[2:])      
        print('{0:<5} {1:<5}'.format(i,oc),end=" ")
        print()
        # hx = (hex(i)[2:])
        # print(f'{hx:2}',end=" ")
        # bn = (bin(i)[2:])
        # print(f'{bn:2}')          

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    # a= 1
    # print(bin(a))
    # print(hex(a))
    # print(oct(a))