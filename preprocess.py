import pandas as pd
import numpy as np
import time
import math

df = pd.read_csv('etymology.csv')
#print(df.iloc[0])
#print(df.shape)
#aim: find just one set of rules
#reltype = subset of all reltypes
#maybe reltype = inherited_from
df_all_eng = df.loc[df['lang'] == 'English']
print(f'shape of all english db: {df_all_eng.shape}')
df_all_eng.to_csv('all_english.csv', index=False)  


df_inherited_from = df.loc[df['reltype'] == 'inherited_from']
#print(df_inherited_from.iloc[0])
#print(df_inherited_from.shape)
#print(df_inherited_from['related_lang'].unique())
#print(len(df_inherited_from['related_lang'].unique()))

#print(df_inherited_from['lang'].unique())
#print(len(df_inherited_from['lang'].unique()))
#so. there are 335 possible 'related_lang' values'

#OHHH. Let's look at just English words, for one

df_english = df_inherited_from.loc[df_inherited_from['lang'] == 'English']

print(df_english['related_lang'].unique())
print(len(df_english['related_lang'].unique()))
#only eighteen. this is so doable!
print(df_english.shape)
print(df_english.iloc[0])


df_english.to_csv('english_related.csv', index=False)  
#so. secondary problem: 
