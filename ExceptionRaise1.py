
def f(a):
    if isinstance(a, int):
        return a**2
    else:
        raise ValueError("a is not an int")
        
        
try:
    print(f(12))

    print(f('a'))
except:
    print("Exception raised")
    
print('The end')