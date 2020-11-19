import pandas as pd
import re
df=pd.read_csv('pokemon_data.csv')
print(df)
print(df.head(3))
print(df.tail(3))
# Get headers

print(df.columns)

print(df.Name[0:5])
print(df[['Name','Type 2','Speed']])
#printing each row

print(df.iloc[0:4])
#indexing
print(df.iloc[2][1])

for index, row in df.iterrows():
        print(index,row['Name'])

print(df.loc[df['Speed']==65])
#getting statistics
print(df.describe())

print(df.sort_values(['Type 1','Speed'],ascending=[0,0]))
print(df.sort_values('Name',ascending=True))
# Make changes to data

df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
print(df.head(5))
df=df.drop(columns=['Total'])
print(df.head(5))
df['Total'] = df.iloc[:,4:10].sum(axis=1)
print(df.head(5))
# Rearrangening columns header
cols = list(df.columns.values)
df = df[cols[0:4]+ [cols[-1]]+cols[4:12]]
df.to_csv('modified.csv',index=False)
#df.to_excel('modified.xlsx',index=False)   SEE GOOGLE
df.to_csv('modified.txt', index= False , sep='\t')
# Filtering Data
new_df=df.loc[(df['Type 1']=='Grass') & (df['Type 2']=='Poison')]
new_df.to_csv('New_modified.csv', index=False)
# reset indexes
new_df= new_df.reset_index()
print(new_df)
# Getting specific name
print(df.loc[df['Name'].str.contains('Mega')])
print(df.loc[~df['Name'].str.contains('Mega')])

print(df.loc[df['Type 1'].str.contains('Fire|grass' , flags=re.I, regex=True)])

# Q : extract name start with 'pi' if you want 'pi' at start put ^pi
print(df.loc[df['Name'].str.contains('^pi', regex=True , flags=re.I)])

#Conditional changes---- Changing names inside a specific column

df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'
# Change any value according to their type
df.loc[df['Type 1'] == 'Flamer', 'Generation'] = 20
df.to_csv('modified11.csv', index=False)
print(df.head(30))

df.loc[df['Total'] > 500,['Generation','Legendary']] = 'TEST VALUE'

print(df.head(30))

#Aggregate Statistics

print(df.groupby(['Type 1']).mean().sort_values('Attack', ascending=False))

print(df.groupby(['Type 1']).sum())
print(df.groupby(['Type 1']).count())

df['count']=1
print(df.head(20))
print(df.groupby(['Type 1','Type 2']).count()['count'])

# working with large data sets

for df in pd.read_csv('modified.csv' , chunksize=5):
    print(df)

 