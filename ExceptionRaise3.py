# Creation of custom exception class thanks to the
# "inheritance" mechanism

class WrongKindOfArgumentError(Exception):
    pass


def f(a):
    if isinstance(a, int):
        return a**2
    else:
        ex=WrongKindOfArgumentError("a is not an int")
        raise ex
        
        
try:
    print(f(12))
    print(f('a'))
except WrongKindOfArgumentError as e:
    print("Exception raised:", e)
    
print('The end')