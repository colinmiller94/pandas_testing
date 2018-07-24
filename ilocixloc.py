import pandas as pd

ufo = pd.read_csv('http://bit.ly/uforeports')

print(ufo.head(3))

print(ufo.iloc[:, :])

