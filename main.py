import pandas as pd
from csv import reader

with open("/Users/sula/Documents/GitHub/PythonCode/Testing.csv", mode='r') as readObject:
    csv_Reader = reader(readObject)

    for row in csv_Reader:
        print(row[0])







#with open("/Users/sula/Documents/GitHub/PythonCode/reply.txt", mode='r') as f:
#    fileTxt = f.readlines()
#    highSchool = fileTxt[0]

#dice = {"1" : highSchool}

#str = dice.get("1")
#print(str)