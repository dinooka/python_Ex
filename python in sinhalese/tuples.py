# consider a tuple as databse table row which consist many data 
person = ('Kim',33,'Hill street','USA','14100233421','Kim')

a = person[0]

print(a)
print(type(person))
print(person.count("Kim"))

# expand a tuple
student = (1,'Sam','male')
index, name, sex  = student

print(index, name)


# we can define a tuple without brackets as well

a_tuple = 1,'hi',

print(type(a_tuple))

print(dir(a_tuple))
