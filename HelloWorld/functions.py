
if False:
    # y = max(10,20)
    # print(y)


    from cgi import print_form

    # user define funcitons
    def sum(a,b):
        return a+b
        
    def mul(a,b):
        print("multipliaction of 2 numbers = " + str(a*b))

    tot = sum(6,5)
    print(tot)

    mul(6,5)


    def myFunc(name):
        print("Hello!, ",name)

    str = input("Enter the name: ")
    myFunc(str)


    def greet(name, msg="Good morning!"):  
        print("Hello", name + ', ' + msg) 

    greet("Mon")

    def add(*args):
        total = sum(args)
        print("Total= ", total)

    add(5,10)

    def greet(*names):
        for name in names:
                print("Hello", name)

    greet('sam','pam','Tim','Ann')

    def add(a, b):
        return a+5, b+5

    t = add(3, 2)
    print(t)

    def myfunction(number):
        return number

    print(myfunction(100))

    def my_function(fname):
        print(fname + " Perera")
    my_function("Anne")

# def greet(name, msg):  
#     print("Hello", name + ', ' + msg) 

# greet("Mon")


# def myfunction(number):
#     return number

# print(myfunction(100))

def factorial1(number):
    if number <= 1: return 1
    return number * factorial1(number-1)

print(factorial1(4));