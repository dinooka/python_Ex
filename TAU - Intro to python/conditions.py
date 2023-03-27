
def add():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a+b)
   

def sub():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a-b)

 
on = True
while on:
    result = input("Enter '+', '-' or 'q' :")

    if result == '+':
        add()
    elif result == '-':
        sub()
    elif result == 'q':
        on = False





# brackets aren't required in python if else statements