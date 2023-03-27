#TODO: Write the functions for arithmatic operations here
#These functions should cover Task 2
from distutils.log import error
from sys import modules

def enter_firstnum():
        return float(input("Enter first number: "))

def enter_secondnum():
        return float(input("Enter second number: "))

def add(a,b):
    ans = a+b
    print(a, " + " , b, " = ",ans)    
    print()

def subtract(a,b):
    ans = a-b
    print(a, " - " , b, " = ",ans)    
    print()

def multiply(a,b):
    ans = a*b
    print(a, " * " , b, " = ",ans)    
    print()

def divide(a,b):
    if(b!=0):
        try:
            ans = a/b
            format_ans = "{:.2f}".format(ans)
            print(a, " / " , b, " = ",format_ans)    
            print()
        except:
            print("division by zero error!!!")
    else:
        print("division by zero error!!!")

def power(a,b):
    ans = a**b
    print(a, " ^ " , b, " = ",ans)    
    print()
    

def remainder(a,b):
    ans = a%b
    print(a, " % " , b, " = ",ans)    
    print()

#-------------------------------------
#TODO: Write the select_op(choice) function here
#This function sould cover Task 1 (Section 2) and Task 3
def select_op(choice):
    return choice


#End the select_op(choice) function here
#-------------------------------------
#This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:

    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")
  

  # take input from the user
    try:
        choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
        print(choice)
        if(select_op(choice) == '#'):
        #program ends here
            print("Done. Terminating")
            exit()
        elif(select_op(choice) == '$'):
            continue

    except:
        print(error)

    # else:
# "Enter first number: "
# "Enter second number: "
# "Not a valid number,please enter again"
# "Unrecognized operation"
# "Something Went Wrong"


    if(select_op(choice) == '+'):
        num1 = enter_firstnum()
        num2 = enter_secondnum()
        add(num1,num2)
    elif(select_op(choice) == '-'):
        num1 = enter_firstnum()
        num2 = enter_secondnum()
        subtract(num1,num2)
    elif(select_op(choice) == '*'):
        num1 = enter_firstnum()
        num2 = enter_secondnum()
        multiply(num1,num2)
    elif(select_op(choice) == '/'):
        num1 = enter_firstnum()
        num2 = enter_secondnum()
        divide(num1,num2)
    elif(select_op(choice) == '^'):
        num1 = enter_firstnum()
        num2 = enter_secondnum()
        power(num1,num2)
    elif(select_op(choice) == '%'):
        num1 = enter_firstnum()
        num2 = enter_secondnum()
        remainder(num1,num2)
    else:
        print("Unrecognized operation")
        