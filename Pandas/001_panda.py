import pandas as pd

# Reaading csv 
df = pd.read_csv('sample4.csv')

# getting max temprature 
# print(df['Temprature'].max()) 

# getting date on which it's rain 
print(df['Date'][df['Events']=='Rain'])
