class TempProcess:
    
    def __init__(self, fileName):
        self.content=dict()
        self.readFromFile(fileName)
            
    def readFromFile(self, fileName):
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
                    if city in self.content:
                        self.content[city].append(temp)
                    else:
                        self.content[city]=[temp]
        except Exception as e:
            raise Exception(f"Problem with the file {fileName}: {e}")
           
    def getTemperatures(self, city):
        cityl=city.lower()
        if cityl in self.content:
            return self.content[cityl]
        else:
            raise Exception(f"Unknown city {city}")
            
    def getMiniMaxi(self, city):
        cityl=city.lower()
        if cityl in self.content:
            #mini,*_, maxi=sorted(self.content[cityl])
            
            return (min(self.content[cityl]),max(self.content[cityl]))
        else:
            raise Exception(f"Unknown city {city}")    
            
    def getAverage(self, city):
        cityl=city.lower()
        if cityl in self.content:
            return sum(self.content[cityl])/len(self.content[cityl])
        else:
            raise Exception(f"Unknown city {city}")
            
    def getNumberOfMeasures(self, city):
        cityl=city.lower()
        if cityl in self.content:
            return len(self.content[cityl])
        else:
            raise Exception(f"Unknown city {city}")
            
    def getNumberOfCities(self):
        return len(self.content)
    
    def saveSummary(self, fileName):
        try:
            with open(fileName,"w") as f:
                for city in self.content:
                    f.write(f"{city.capitalize()}: {self.content[city]} Average:{self.getAverage(city):.2f}\n")
        except Exception as e:
            raise Exception(f"Problem with the file {fileName}: {e}")
    

if __name__ == "__main__":
    
    tp=TempProcess("cities.txt")
    print(tp.content)
    print(f"Geneva appears {tp.getNumberOfMeasures('Geneva')} time in the file")
    print(f"The average of the temperature in Nyon is {tp.getAverage('Nyon'):.2f}")
    print(f"{tp.getNumberOfCities()} different cities are present in the file")
    print(f"The temperatures recorded in Lausanne are {tp.getTemperatures('Lausanne')}")
    print(f"Mini and Maxi temperatures recorded in Lausanne: {tp.getMiniMaxi('Lausanne')}")
    tp.saveSummary("data_summary.txt")
    



