import pandas as pd

data = {'First Column Name':  ['First value', 'Second value',...],
        'Second Column Name': ['First value', 'Second value',...],

        }

df = pd.DataFrame (data, columns = ['First Column Name','Second Column Name',...])

print (df)