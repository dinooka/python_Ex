
dict = {'001':'sam','010':'Ann',777:"peppa pig"}
dict['123'] ='Idaho'

'''
print(dict)

y = dict['123']
z = dict[777]
print(y)

# get the value of a key
print("Get the value of the Key(123): {}".format(dict.get('123')))

# items() returns all the key & value pairs in the dictionary
items = dict.items()
print(items)

# keys() returns all the keys in the dictionary
keys = dict.keys()
print(keys)

# values() returns all the values in the dictionary
val = dict.values()
print(val)

# popitem() removes the last item frm the dic
print(dict.popitem())
print(dict)

# pop() removes the item frm the dic using the 'key'
print(dict)
dict.pop(777)
print(dict)

print(dict.setdefault(777))
print(dict)
print(dict.setdefault("333","bacon"))
print(dict)


new_items = {"new 1":1.33, "new 2":56.88, "new 3":89.04}
dict.update(new_items)
print(dict)

print("Original list :{}".format(dict))
update_list = {"t1":"MR","t2":"RW","t3":"AKD"}
dict.update(update_list)
print(dict)

dict.update(t1="GR",cookies="clear")
print(dict)

'''

postal_codes = {10290:"boralesgamuwa",10300:"Piliyandala", 10280:"Maharagama",10300:"Maharagama"}

# in - this will search for the text in "KEY"

print(10290 in postal_codes)
print("Piliyandala" in postal_codes)