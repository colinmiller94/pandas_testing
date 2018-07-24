import unittest
import pandas as pd
import nose.tools


url = 'https://www.usinflationcalculator.com/inflation/historical-inflation-rates/'
fn = 'Inflation.xlsx'
df = pd.read_html(url)[0]
sn = 'Sheet 1'
writer = pd.ExcelWriter(fn)

df.to_excel(writer,sn)
writer.save()

xl = pd.ExcelFile(fn)
df2 = xl.parse(sn)

df2[0][0] = 'JSLKDFJ:LKJ'

class TestPd(unittest.TestCase):
    pass




for i in range(2, len(df) -1):
    for j in range(1, len(df.columns)):
        testmethodname = 'test_df{}_{}'.format(i, j)
        testmethod = lambda self: self.assertEqual(float(df.iloc[i,j]),float(df2.iloc[i,j]))
        setattr(TestPd, testmethodname, testmethod)



# def test():
#     for i in range(len(df.columns)):
#         for j in range(len(df)-1):
#             yield nose.tools.assert_equals, df[i][j], df2[i][j]
#
#
# test()

#
# class TestPd(unittest.TestCase):
#     def test_ex(self):
#         self.assertEqual(df[0][6],df2[0][6])

if __name__ == "__main__":
    unittest.main()
