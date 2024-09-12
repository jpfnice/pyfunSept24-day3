
def f(a):
    if isinstance(a, int):
        return a**2
    else:
        ex=ValueError("a is not an int")
        raise ex
        
        
try:
    print(f(12))

    print(f('a'))
except:
    print("Exception raised")
    
print('The end')