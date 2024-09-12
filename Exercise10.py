
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

class Stack:
    def __init__(self, maxi):
        # definition and initialization of the 2 attributes
        if isinstance(maxi, int) and maxi > 0:
            self.maximumSize=maxi
        else:
            print("Wrong max size given !!")
            self.maximumSize=10
        self.data=[]
        
    def __repr__(self):
        # return a string representation of the stack
        return f"({len(self)}/{self.maximumSize}) {self.data}"
    
    def __len__(self):
        # returns the length of the Stack (the length of data)
        return len(self.data)
    
    def push(self, element):
        # add a element at the end of data if the maximumSize is not
        # exceeded 
        # if the maximumSize is reached, push() print an error message 
        if len(self) < self.maximumSize:
            self.data.append(element)
        else:
            print("Error: maximum size reached !!!")
            
    def pop(self):   
        # return and remove the element currently at the end of data 
        # if data is empty, pop() print an error message and return 
        # a None value
        if len(self) == 0 :
            print("Error: the Stack is empty !!!")
            return None
        else:
            return self.data.pop()
    
    
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

