import numpy as np
import pandas as pd
df = pd.read_csv('1200 coded reports.csv')
print(df)
print (df.tail())
print(df.shape)
print(df['Upstream measurees']=='Machinery and Equipment')

