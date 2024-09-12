
class listPLus(list): # listPlus inherit from list
   def removeAll(self, element):
       while element in self:
           self.remove(element)
   def __add__(self, list2): # correspond to the + operator
        newList=[]
        if len(self) > len(list2):
            index=0
            while index < len(list2): 
                newList.append(self[index]+list2[index])
                index+=1
            while index < len(self): 
                newList.append(self[index])
                index+=1
        else:
            index=0
            while index < len(self): 
                newList.append(self[index]+list2[index])
                index+=1
            while index < len(list2): 
                newList.append(list2[index])
                index+=1
            
        return newList

l1=listPLus((5,6,7))
print(l1)
l1.append(5)
print(len(l1))
print(l1)
l1.removeAll(5)
print(l1)


l2=listPLus((8,9,10))
print(l2)

l3=l1+l2

print(l3)