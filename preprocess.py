import pandas as pd
import numpy as np
import time
import math


#preprocessing functions:
def gen_info(df):
    print(f'Num. of Instances: {df.shape[0]}')
    print(f'Sample Instance: {df.iloc[13]}')
    related = df['related_lang'].unique()
    print(f'There are {len(related)} Languages Inherited From: {related}')

def preprocess_df(df):

    #for interest

    df = df.loc[(df['reltype'] == 'inherited_from')]
    print(df.shape)#debug
    print(df.iloc[0])#debug
    df = df.loc[df['parent_position'] == 0.0]
    df['term'] = df['term'].str.lower()


    unique_words = df['term'].unique()
    print(unique_words)
    print(unique_words[0])
    terms_to_keep = [None if (' ' in term) else term for term in unique_words]
    df = df.loc[df['term'].isin(terms_to_keep)]
    return df


def get_english(filename):
    df = pd.read_csv(filename)
    df_all_eng = df.loc[df['lang'] == 'English']
    print(f'shape of all english db: {df_all_eng.shape}')
    df_all_eng.to_csv('all_english.csv', index=False)  

if __name__ == "__main__":
    get_english('etymology.csv')

