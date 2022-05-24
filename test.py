import pandas as pd

df=pd.read_excel('trainingset.xls')
df=pd.DataFrame(df,columns=['A','B','C'])
dict={}
df = df.reset_index()  # make sure indexes pair with number of rows
for index, row in df.iterrows():
    dict[row['A']]=row['B']/(row['B']+row['C'])
print(dict)