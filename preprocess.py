import pandas as pd
import numpy as np
import time
import math

df = pd.read_csv('etymology.csv')

df_all_eng = df.loc[df['lang'] == 'English']
print(f'shape of all english db: {df_all_eng.shape}')
df_all_eng.to_csv('all_english.csv', index=False)  

def sample_func():
    print('sample function!')