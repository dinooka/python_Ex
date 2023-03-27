import re

# ^$     -> describe the position
# \w, [a-z]     -> describe chatacters
# +*{9}         -> describe number of occurences

# char sets
# ^     -> start of a string ex: ^Mr : all texts start with Mr
# $     -> end of a string ex: Perera$ : all texts end with perera
# \d     -> search for a digit[0-9] in a text anywhere
# \s     -> search for a single space in a text anywhere
# \w     -> match a-z,A-Z,0-9, _

# Quantifiers
# {n}   -> n occurences

names = ['Ann','Sam hunt','Tom Cruise','Penny','Ross Geller',
         'Chandler M Bing']

# find names with first & last names
pattern = '^\w+\s+\w+$'
# name start with 'c'
regex = 'C\w'

for i in names:
    result = re.search(regex,i)
    if result:
        print(i)
        # print(result.start())
        # print(result.end())
        print(result.span())
        print(result.group())
