import pandas as pd

df = pd.read_csv('instagram_data.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(df)

print(df.head(5))
print(df.tail(3))

print(df.describe())
print(df.shape)
print(df.dtypes)

print(df.iloc[0:6])
print(df.iloc[1:5])

print(df.loc[df["comments"]>=500])
print(df.loc[df["likes"]<100000])
print(df.loc[df["username"]=='cyarine'])

result = (df["username"]=='kenzas') & (df["likes"]>100).shape[0]
print(result)


dupe= df.duplicated().sum()
print(dupe)

unique_count = df["username"].unique()
print(unique_count)

print(df.columns)

df.to_csv("demo.csv")
