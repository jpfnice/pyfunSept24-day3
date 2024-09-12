import math

class Point: # __new__() __init__() __repr__() __eq__() ....
    def __init__(self,valx=0, valy=0):
        self.x=valx
        self.y=valy
    def __repr__(self):
        return f"<{self.x},{self.y}>"
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)
    def __eq__(self, other):
        return self.x==other.x and self.y == other.y
    def clear(self):
        self.x=0
        self.y=0
    def distance(self, other):
        return math.sqrt((other.y-self.y)**2 + (other.x-self.x)**2)

if __name__ == "__main__":
    p1=Point(2,3)   
    # l=list() d=dict()
    # 1) p1=Point.__new__()
    # 2) p1.__init__(2,3)
    # 3) __init__(p1,2,3)
    
    print(p1.x)
    print(p1.y)
    print(p1) # <2,3>
    # 1) print(str(p1))
    # 2) print(p1.__repr__())
    # 3) print(__repr__(p1))
    
    p2=Point()
    # 1) p2=Point.__new__()
    # 2) p2.__init__()
    
    print(p2.x)
    print(p2.y)
    print(p2) # <0,0>
    
    p2.x=12
    p2.y=10
    print(p2) # <12,10>
    
    p3=p2+p1 
    # 1) p3=p2.__add__(p1) 
    # 2) p3=Point.__add__(p1,p2)
    
    print("p3:",p3) # <14,13>
    
    d=p1.distance(p2)
    print(d)
    
    p2.clear() 
    print(p2) # <0,0>
    
    p4=Point(2,0)
    
    print("p2==p4", p2 == p4)
