
data=[123, 678, 899, 899, 1000]

try:
    index=input("Please enter an int in the range [0,4]: ")
    index=int(index)
    
    print("At position", index, "there is the element", data[index])
except ValueError as e:
    print("A ValueError is detected:", e)
except IndexError as e:
    print("An IndexError is detected:", e)
else:
    print("Else part")
finally:
    print("Always printed")

print("The end")