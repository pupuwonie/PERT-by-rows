import csv
import pandas as pd
import numpy as np

def file(data):
    table = pd.read_excel(data)
    df = pd.DataFrame(table)
    df['duration'] = np.round((df['a'] + 4*df['m'] + df['b'])/6, 2)
    df['variance'] = np.round(np.square((df['b']-df['a'])/6), 2)
    return df

df=file() #input file to solve
df.to_excel() #input the name of the file to export