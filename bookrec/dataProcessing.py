# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 16:04:49 2023

@author: Zane Knightwood
"""

# Creates a dataframe from the dataset and edits it for use by the program.

import pandas as pd
from c964CapstoneZK.settings import BASE_DIR

def getDF():
    file_path = BASE_DIR / 'staticfiles' / 'GoodReads_100k_books.csv'
    print(file_path)
    df = pd.read_csv(file_path, sep=',')
    df = df.dropna()
    return df
