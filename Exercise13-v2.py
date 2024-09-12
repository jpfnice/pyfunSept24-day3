content=dict() # A global dict 
         
def readFromFile(fileName):
    try:
        with open(fileName) as f:
            f.readline()# To skip the first line
            for line in f:
                result=line.split()
                if len(result) != 2:
                    continue
                city=result[0].strip().lower()
                try:
                    temp=float(result[1].strip())
                except ValueError as e:
                    print(f"Wrong temperature format: {e}")
                    continue
                if city in content:
                    content[city].append(temp)
                else:
                    content[city]=[temp]
    except Exception as e:
        raise Exception(f"Problem with the file {fileName}: {e}")
       
def getTemperatures(city):
    cityl=city.lower()
    if cityl in content:
        return content[cityl]
    else:
        raise Exception(f"Unknown city {city}")
        
def getAverage(city):
    cityl=city.lower()
    if cityl in content:
        return sum(content[cityl])/len(content[cityl])
    else:
        raise Exception(f"Unknown city {city}")
        
def getMinimum(city):
    cityl=city.lower()
    if cityl in content:
        return min(content[cityl])
    else:
        raise Exception(f"Unknown city {city}")
        
def getNumberOfMeasures(city):
    cityl=city.lower()
    if cityl in content:
        return len(content[cityl])
    else:
        raise Exception(f"Unknown city {city}")
        
def getNumberOfCities():
    return len(content)

def saveSummary(fileName):
    try:
        with open(fileName,"w") as f:
            for city in content:
                f.write(f"{city.capitalize()}: {content[city]} Average:{getAverage(city):.2f}\n")
    except Exception as e:
        raise Exception(f"Problem with the file {fileName}: {e}")
        

# A small test program:
    
readFromFile("cities.txt")

print(content)

print(f"Geneva appears {getNumberOfMeasures('Geneva')} time in the file")
print(f"The average of the temperature in Nyon is {getAverage('Nyon'):.2f}")
print(f"The minimum of the temperature in Nyon is {getMinimum('Nyon'):.2f}")
print(f"{getNumberOfCities()} different cities are present in the file")
print(f"The temperatures recorded in Lausanne are {getTemperatures('Lausanne')}")

saveSummary("data_summary.txt")









