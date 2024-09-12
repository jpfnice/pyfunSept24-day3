
# myFile=open("data.txt")

# for line in myFile:
#     print(line)
# myFile.close()


with open("data.txt") as myFile:
    # text=myFile.read()
    # print(text)
    print("Position:",myFile.tell())
    text=myFile.read(5)
    print("Position:",myFile.tell())
    print(text)
    text=myFile.read(5)
    print("Position:",myFile.tell())
    print(text)
    myFile.seek(0)
    print("Position:",myFile.tell())
    text=myFile.read(5)
    print("Position:",myFile.tell())
    print(text)
    line=myFile.readline()
    print(line)

print("The end")