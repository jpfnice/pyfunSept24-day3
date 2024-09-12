
# myFile=open("data.txt")

# for line in myFile:
#     print(line)
    
# myFile.close()

# 'r' 'w' 'a' 'r+' 'w+' 'a+' 'br' 'bw' 'ba' ...
with open("output.txt", "a") as myFile:
   myFile.write("First text\n")
   myFile.write("Second text\n")
   print("Use of the print function", file=myFile)
   
print("The end")