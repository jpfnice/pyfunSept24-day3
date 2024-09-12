# Option 1: open(), list(), map(), set(), str.split()

fic=open("numbers.txt")

numbers=[]
for line in fic:
    result=line.split(":")
    result=list(map(float, result))
    numbers+=result
    
fic.close()

numbersSet=set(numbers)
print(numbersSet)

# Option 2: with the help of pandas: read_csv(), set(), array.flatten()

import pandas

df=pandas.read_csv("numbers.txt", sep=":", header=None)
print(set(df.values.flatten()))