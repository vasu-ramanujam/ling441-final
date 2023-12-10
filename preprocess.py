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
    df = df.loc[df['reltype'] == 'inherited_from']
    df = df.loc[df['parent_position'] == 0.0]
    #df = df.loc[df['term'].str[0] != '-']
    #df = df.loc[df['term'].str[-1] != '-']
    df = df.drop(df.loc[df['term'].str.contains(' ', regex=False)])

    unique_words = df['term'].unique()
    entry_per_word = np.zeros_like(unique_words)
    for i, w in enumerate(unique_words):
        df_word = df.loc[df['term'] == w]
        entry_per_word[i] = df_word.shape[0]
    terms_to_keep = unique_words[entry_per_word == 1]
    df = df.loc[df['term'].isin(terms_to_keep)]
    return df


def get_english(filename):
    df = pd.read_csv(filename)
    df_all_eng = df.loc[df['lang'] == 'English']
    print(f'shape of all english db: {df_all_eng.shape}')
    df_all_eng.to_csv('all_english.csv', index=False)  

if __name__ == "__main__":
    get_english('etymology.csv')