
"""
Definition of a new kind of collection: a Stack

A Stack is a mutable collection
A Stack will have a maximum size
In a Stack the only element you can have access to is the one "on top" of the Stack
When you insert a new element in a Stack it is always placed "on top" of the Stack

Attributes:
    maximumSize: an int
    data: an list
Methods:
    __init__(self, maxSize) -> Nothing to return
    __repr__(self) -> return a str
    __len__(self) -> return a int
    push(self, element) -> Nothing to return
    pop(self) -> return the object currently on top of the Stack
    
"""

s1=Stack(10) # s1 is a Stack with a maximum size of 10

s1.push(23)
s1.push("Hello")
s1.push(True)

print(s1) # (3/10) [23,"Hello",True]

print(len(s1)) # 3 # len(s1) => s1.__len__()

top=s1.pop()
print(top) # True

print(s1) # (2/10) [23,"Hello"]
print(len(s1)) # 2

