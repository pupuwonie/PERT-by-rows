import csv
import pandas as pd
import numpy as np

def file(data):
    table = pd.read_excel(data)
    df = pd.DataFrame(table)
    df['duration'] = np.round((df['a'] + 4*df['m'] + df['b'])/6, 2)
    df['variance'] = np.round(np.square((df['b']-df['a'])/6), 2)
    return df

df=file('multiply csv/PERT-by-rows/pert data.xlsx')
df.to_excel("output.xlsx")