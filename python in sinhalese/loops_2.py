# iterating data structures
# use enumearte() to print index & value
# dictionary
postal_codes = {
    10290:"Boralesgamwua",10280:"Maharagama",10270:"Piliyandala"
    }

# print(postal_codes[10290])

# 1st method
for code in postal_codes:
    city = postal_codes[code]
    # print(code,city)
    
# 2nd method  
for code,city in postal_codes.items():
    # print(code, city)  
    pass
# 3rd method
for i,v in enumerate(postal_codes.items()):
    code, city = v
    print(i,code,city)

#set
marks = {22,23,25,27,76}

for m in marks:
    print(m)

# tuple

t = (1,'Ann',True,'F')

# print(type(t))
for i,v in enumerate(t):
    print(i,v)

