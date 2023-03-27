
weight = int(input("Weight : "))

unit = input("(k)g or (L)bs : ")

if unit == 'l' or unit == 'L' :
    print("Weight in kg : " , float(weight*0.45))

elif unit == 'k' or unit== 'K':
    print("Weight in lb : " , float(weight*2.20))

else :
    print("Please enter the unit in lb or kg")






















