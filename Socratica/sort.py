elements = ["Oxygen","Sulpher","Selenium","Telenium","Polonium"]

elements.sort()
print(elements)

elements.reverse()
print(elements)

# sorted function
sblock=['H','Li','Na','K','Rb','Xe','Fr']
a=sorted(sblock)
print(a)

# sort a list using a key
cricketer = [("AB",12344,54.53),("Sanga",14223,56.21),
             ("Kallis",11889,61,33),("Smith",9877,44.88)]
runs = lambda crick : crick[1]
cricketer.sort(key = runs,reverse=True)
print(cricketer)


# sorted()
phones = ['Apple','bpple','applE','APple','apple']
# phones = ['Samsung','Apple','Xiamoi','Nokia','Pixel','Realme']
print(sorted(phones))

tablets = 'panadol','piritin','Daktarin','Pevisone','Thyronorm'
# o/p is a list
print(sorted(tablets))

print(sorted("mahindamahattya"))