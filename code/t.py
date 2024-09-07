import pandas as pd


df = pd.read_excel(
    "C:\\Users\\Rohit Chess\\Desktop\\Python-Programming\\Lab Programs\\table.xlsx")
print(df.mean())
print(df.std())
'''
Output: -
Data    54.166667
dtype: float64
Data    6.080022
dtype: float64
'''