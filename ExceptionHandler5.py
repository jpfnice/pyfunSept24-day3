
data=[123, 678, 899, 899, 1000]

while True:
    try:
        
        index=input("Please enter an int in the range [0,4]: ")
        index=int(index)
        print("At position", index, "there is the element", data[index])
        break
    except Exception as e:
        print("An Exception is detected:", e)
    else:
        print("Else part")
    finally:
        print("Always printed")

print("The end")