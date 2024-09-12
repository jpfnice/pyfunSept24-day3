
class StackError(Exception):
    pass
class StackSizeError(StackError):
    pass
class StackFullError(StackError):
    pass
class StackEmptyError(StackError):
    pass

class Stack:
    def __init__(self, maxi):
        # definition and initialization of the 2 attributes
        if isinstance(maxi, int) and maxi > 0:
            self.maximumSize=maxi
        else:
            raise StackSizeError(f"Wrong max size given: {maxi} !!")
        self.data=[]
        
    def __repr__(self):
        # return a string representation of the stack
        return f"({len(self)}/{self.maximumSize}) {self.data}"
    
    def __len__(self):
        # returns the length of the Stack (the length of data)
        return len(self.data) 
    
    def __contains__(self, element):
        
        return element in self.data 
    
    def push(self, element):
        if len(self) < self.maximumSize:
            self.data.append(element)
        else:
            raise StackFullError("Error in push(): maximum size reached !!!")
            
    def pop(self):
        if len(self) == 0 :
            raise StackEmptyError("Error in pop(): the Stack is empty !!!")
        else:
            return self.data.pop()
    
    
try:
    s1=Stack(10) # s1 is a Stack with a maximum size of 10

    s1.push(23)
    s1.push("Hello")
    s1.push(True)
    
    if 23 in s1:
        print("Present")
        
    print(s1) # (3/10) [23,"Hello",True]
    
    print(len(s1)) # 3 # len(s1) => s1.__len__()
    
    top=s1.pop()
    print(top) # True
    
    print(s1) # (2/10) [23,"Hello"]
    print(len(s1)) # 2
except StackError as e:
    print("Problem encountered:", e)
