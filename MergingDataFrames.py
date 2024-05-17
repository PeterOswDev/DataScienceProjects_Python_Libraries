import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

df1 = pd.read_csv(r'C:\Users\oswpe\Desktop\Pandas_Python\LOTR.csv')
print(df1)

print('*******************************')
df2 = pd.read_csv(r'C:\Users\oswpe\Desktop\Pandas_Python\LOTR 2.csv')
print(df2)
print('********************************')

mergeFunction = df1.merge(df2)
print(mergeFunction)
print('***************************')
mergeFunction_1 = df1.merge(df2, how='inner', on= 'FellowshipID')
print(mergeFunction_1)
print('***************************')
mergeFunction_2 = df1.merge(df2, how='inner', on = ['FellowshipID', 'FirstName'])
print(mergeFunction_2)
print('***************************')
mergeFunction_3 = df1.merge(df2, how = 'outer')
print(mergeFunction_3)
print('*******************************')
mergeFunction_4 = df1.merge(df2, how = 'left')
print(mergeFunction_4)

print('*******************************')
mergeFunction_5 = df1.merge(df2, how = 'right')
print(mergeFunction_5)

print('*******************************')
mergeFunction_6 = df1.merge(df2, how = 'cross')
print(mergeFunction_6)
joinFunction_1 = df1.join(df2, on = 'FellowshipID', how = 'outer', lsuffix = '_Left',rsuffix = '_Right' )

print(joinFunction_1)
print('*******************************')
df4 = df1.set_index('FellowshipID').join(df2.set_index('FellowshipID'),lsuffix = '_Left',rsuffix = '_Right', how = 'outer')
print(df4)

print('*******************************')
concatenateFunction_1 = pd.concat([df1,df2])
print(concatenateFunction_1)

print('*******************************')
concatenateFunction_2 = pd.concat([df1,df2], join='outer')
print(concatenateFunction_2)

print('*******************************')
concatenateFunction_3 = pd.concat([df1,df2], join='outer', axis = 1)
print(concatenateFunction_3)

print('*******************************')
appendFunction_1 = df1._append(df2)
print(appendFunction_1)

print('*******************************')






