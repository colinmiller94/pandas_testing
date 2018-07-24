import pandas as pd

df1 = pd.DataFrame({'a': [1,2,3,4,5]})
df2 = pd.DataFrame({'a':[6,7,8,9,10]})

print(df1)
print(df2)

print(df1 + df2)

df1.loc[3,'a'] = 12
df1.loc[3,'a'] = 4

exp_res = pd.DataFrame({'a' :[7,9,11,13,15]})

pd.testing.assert_frame_equal((df1+ df2), exp_res, check_names = False)