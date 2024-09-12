
def sub(op1, op2):
    return op1-op2

print(sub(12, 34)) # positional arguments

print(sub(op2=12, op1=34)) # named arguments


def example(**args):
    print(args)
    
example()
example(a=12)
example(a=34,file="text.txt",value=6.7)