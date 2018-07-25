import pandas as pd

#1
df = pd.read_csv('cars.csv', sep = ';')


#2
print(df.columns.tolist())



#3
#print(df['Car'])
print(df)
df['MPG'] = df['MPG'].iloc[1:].astype(float)
max_mpg = df[df.MPG == df.MPG.max()]

print(df)

#max = df[df['MPG'].max()]


print('max:',  max_mpg.loc[:,'Car':'MPG'])
