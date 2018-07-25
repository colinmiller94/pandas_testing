import pandas as pd

df1 = pd.DataFrame({'a': [1,2,3,4,5], 'b': [0, None, 1, 2 ,3]})
df2 = pd.DataFrame({'a':[6,7,8,9,10], 'b': [0, None, 3, 1 ,3]})

# print(df1)
# print(df2)
#
# print(df1 + df2)

df1.loc[3,'a'] = 12
df1.loc[3,'a'] = 4

#df1.iloc[3,0] = 32



print(df1)

exp_res = pd.DataFrame({'a' :[7,9,11,13,15], 'b': [0, None, 4, 3 ,6]})




columns = df1.columns

for column in columns:
    pd.testing.assert_series_equal((df1+df2)[column], exp_res[column])


#pd.testing.assert_frame_equal((df1+ df2), exp_res)





