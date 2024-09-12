

def mySum(*args):
    total=0
    for e in args:
        total += e
    return total


print(mySum())

print(mySum(2,3))

print(mySum(4,5,6,7))

l=list(range(2,10))
print(l)

print(mySum(*l))






