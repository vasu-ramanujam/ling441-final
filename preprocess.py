import pandas as pd
import numpy as np
import time
import math

def sample_func():
    print('sample function!')


#preprocessing functions:
def gen_info(df):
    print(f'Num. of Instances: {df.shape[0]}')
    print(f'Sample Instance: {df.iloc[13]}')
    related = df['related_lang'].unique()
    print(f'There are {len(related)}Languages Inherited From: {related}')


def get_related(df):
    return df.loc[df['reltype'] == 'inherited_from' and df['parent_position'] == 0.0]





def get_english(filename):
    df = pd.read_csv(filename)
    df_all_eng = df.loc[df['lang'] == 'English']
    print(f'shape of all english db: {df_all_eng.shape}')
    df_all_eng.to_csv('all_english.csv', index=False)  

if __name__ == "__main__":
    get_english('etymology.csv')