import pandas as pd

dataCSV = pd.read_csv("/Users/sula/Documents/GitHub/PythonCode/Testing.csv")
dataList = dataCSV.iloc[:, 'How are you feeling?']
print(dataList)

with open("/Users/sula/Documents/GitHub/PythonCode/reply.txt", mode='r') as f:
    fileTxt = f.readlines()
    highSchool = fileTxt[0]

dice = {"1" : highSchool}

str = dice.get("1")
print(str)