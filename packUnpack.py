

def minMax(data):
    return (min(data), max(data))


d=[6,2,3,6,10,19,1]

result=minMax(d)
print(result)

print(result[0])

mini,maxi=minMax(d) # unpacking
print(mini)
print(maxi)

d=[6,2,3,10]

first, *other, last=d
print(first)
print(last)
print(other)

d=[6,2,3,8,9,19,10,10]
first, *other, last=d
print(first)
print(last)
print(other)

d=[6,10]
first, *other, last=d
print(first)
print(last)
print(other)




