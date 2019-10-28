import pandas
df = pandas.read_csv('complete.csv')

print(df.loc[(df['price']>=100)  & (df['price'] <=150)])

