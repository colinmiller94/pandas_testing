import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

web_stats = {'Day':[1,2,3,4,5,6], 'Visits':[43,54,34,35,54,65], 'Bounce_Rate': [76,56,33,54,76,23]}

df = pd.DataFrame(web_stats)


df.set_index('Day', inplace = True)

df['visits_sq'] = df['Visits'] ** 2
#
# print(df.Visits.tolist())


# df = pd.read_csv('zillow.csv')
# df.set_index('Date', inplace = True)
#
# df.to_csv('newcsv.csv')
# df = pd.read_csv('newcsv.csv', index_col = 0)
# df.columns =['Austin HPI']
#
# print(df.iloc[0][1])

print(df.ix[df['Visits']>60])
print(df[df['Visits'] != 43])

# print(df.loc[2:,'Visits':'Bounce_Rate'])
# print(df.iloc[0:,1:])