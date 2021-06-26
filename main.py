import pandas as pd

dataCVS = pd.read_csv("/Users/sula/Desktop/Testing.csv")
print(dataCVS)

with open("/Users/sula/Documents/GitHub/PythonCode/reply.txt", mode='r') as f:
    fileTxt = f.readlines()
    highSchool = fileTxt[0]

dice = {"1" : highSchool}

str = dice.get("1")
print(str)