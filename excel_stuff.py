import unittest
import pandas as pd


url = 'https://www.usinflationcalculator.com/inflation/historical-inflation-rates/'
fn = 'Inflation.xlsx'
df = pd.read_html(url)[0]
sn = 'Sheet 1'
writer = pd.ExcelWriter(fn)

df.to_excel(writer,sn)
writer.save()

xl = pd.ExcelFile(fn)
df2 = xl.parse(sn)


# print(len(df.columns))
#
# print(df)
#
# for i in range(len(df.columns)):
#     for j in range(len(df)-1):
#         #print(df[i][j],df2[i][j])
#         print(df.iloc[j,i])
#         if df[i][j] != df2[i][j]:
#             print('HERE')
#

#
# print(df)
# print(df[0][7])

lst =[0,1,2,3,4,5,6,7]

print([lst[0]] + lst[:-1])