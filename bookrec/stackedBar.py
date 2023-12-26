# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 11:06:07 2023

@author: Zane Knightwood
"""

# Creates a stacked bar graph showing the distribution of matching elements in the recommended book list.

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from bookrec import bookSorting
import os

def make_bar(user_book):
    if os.path.exists('/home/zaneknightwood/stacked_bar.png'):
        os.remove('/home/zaneknightwood/stacked_bar.png')
    
    book_recommendations = bookSorting.get_book_rec_augepara(user_book)
    bar_values = book_recommendations[1]
    book_recommendations = book_recommendations[0]
    groups = []
    values_au =[]
    values_ge =[]
    values_pa = []
    values_ra = []
    count = 1

    for i in book_recommendations:
        groups.append(str(i.title))

    for b in book_recommendations:
        for i in bar_values:
            if i[0] == b.bookId and i[1] == 'au':
                values_au.append(i[2])
        if len(values_au) != count:
            values_au.append(0)
        for i in bar_values:
            if i[0] == b.bookId and i[1] == 'ge':
                values_ge.append(i[2])
        if len(values_ge) != count:
            values_ge.append(0)
        for i in bar_values:
            if i[0] == b.bookId and i[1] == 'pa':
                values_pa.append(i[2])
        if len(values_pa) != count:
            values_pa.append(0)
        for i in bar_values:
            if i[0] == b.bookId and i[1] == 'ra':
                values_ra.append(i[2])
        if len(values_ra) != count:
            values_ra.append(0)
        count += 1
        
    fig, ax = plt.subplots()
    

    ax.bar(groups, values_au, label = 'Matching Authors', color = '#8696a9')
    ax.bar(groups, values_ge, bottom = values_au, label = 'Matching Genres', color = '#8f9e8a')
    ax.bar(groups, values_pa, bottom = values_ge, label = 'Matching Page Count', color = '#cdb775')
    ax.bar(groups, values_ra, bottom = values_pa, label = 'Matching Rating', color = '#d8b3b3')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    ax.legend()
    plt.tight_layout()
    plt.savefig('stacked_bar.png', dpi=100)
    plt.clf()