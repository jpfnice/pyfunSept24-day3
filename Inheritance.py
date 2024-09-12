
class Stack(list): # Stack inherit from list
    def __init__(self, maxi):
        # definition and initialization of the 2 attributes
        if isinstance(maxi, int) and maxi > 0:
            self.maximumSize=maxi
        else:
            print("Wrong max size given !!")
            self.maximumSize=10

    def push(self, element):
        if len(self) < self.maximumSize:
        # or if len(self.data) < self.maximumSize:
            self.append(element)
        else:
            print("Error: maximum size reached !!!")

s1=Stack(20) 
s1.append(56)
s1.append(56)
s1.append(56)
s1.append(56)
s1.insert(0,100)
print(s1[0])

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
