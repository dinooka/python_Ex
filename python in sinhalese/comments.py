# comment
"unless we assign this to a var this will consider as a comment"
"""
multiline
comments
"""

print("Hi!")

def add(x:int, y:int=2)->int:
    "this method returns the sum of 2 int"
    return x + y

print(add(4,5))
# FIXME = below line
# BUG = below line
print(add(4))