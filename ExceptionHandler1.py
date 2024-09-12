
data=[123, 678, 899, 899, 1000]

try:
    index=input("Please enter an int in the range [0,4]: ")
    index=int(index)
    
    print("At position", index, "there is the element", data[index])
except:
    print("Exception handler is called")

print("The end")