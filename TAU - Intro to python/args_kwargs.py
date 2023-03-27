'''
# positional arguments
def info(name,age,city):
    print("{} who is {} years old lives in {}.".format(name,age,city))


info("Sam",22,"Fort")
# info(22) # getting an error due to missing 2 positional arguments


# keyword arguments
def keyword_arguments(name, score, venue="Sydney"):
    print("{} played a {} at {}.".format(name,score,venue))


keyword_arguments("Smith",122)
keyword_arguments(score=134, name="Sanga", venue="SSC")


# args - pass unlimited positional argumetns
def total(*args):
    print(sum(args))

total(1,2,3)
total(1,2,3,10,15,16)

# **kwargs -  pass unlimited keyword argumetns

def application(**kwargs):
    print(kwargs)

application(ttt="Tom", age = 66, Marks = 79)

'''
# combining all argument types 
# order should be positional arguments, *args, **kwargs

def arg_combination(fname,lname,*args,**kwargs):
    # print("{} {} works at {} & has monthly income .".format(fname,lname,*args))
    print("{} {} works at {}.".format(fname,lname,*args))
    
    for k, v in kwargs.items():
        print("his {} is {}.".format(k,v))

arg_combination("Steve","Smith","Cricket australia", salary=30000)

def application(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}. Her email is {}.".format(fname, lname, company, email))

# application("Jess", "Ingrass", "mail @ mail.com","Amazon", 75000, hire_date = "September 2010", )