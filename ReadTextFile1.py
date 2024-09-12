
# myFile=open("data.txt")

# for line in myFile:
#     print(line)
    
# myFile.close()


with open("data.txt") as myFile:
    for line in myFile:
        print(line)

print("The end")