import pandas as pd

dataCSV = pd.read_csv("/Users/sula/Documents/GitHub/PythonCode/Testing.csv", index_col="Timestamp")
dataPerson1 = dataCSV.loc["Person 1"]
dataList = dataPerson1.to_list()

if(dataList[0] == "Frustrated"):
    print("Fru")


#with open("/Users/sula/Documents/GitHub/PythonCode/reply.txt", mode='r') as f:
#    fileTxt = f.readlines()
#    highSchool = fileTxt[0]

#dice = {"1" : highSchool}

#str = dice.get("1")
#print(str)