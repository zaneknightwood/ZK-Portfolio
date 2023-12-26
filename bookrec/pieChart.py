# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 11:06:07 2023

@author: Zane Knightwood
"""

# Creates a pie chart representing a comparison of how closely the recommended books match the user's book.

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as pieplt
from bookrec import bookSorting
import os

pie_colors = ['#beb2df', '#86bef0', '#8f9e8a', '#8696a9', '#d8b3b3', '#cdb775']


def make_pie(user_book):
    if os.path.exists('/home/zaneknightwood/pie_chart.png'):
        os.remove('/home/zaneknightwood/pie_chart.png')

    book_recs = bookSorting.get_recommended_books(user_book)
    data = []
    pie_labels = []
    for book in book_recs:
        data.append(book.percent_match / 6)
        pie_labels.append(book.title)

    pieplt.pie(data, labels = pie_labels, colors = pie_colors)
    pieplt.savefig('pie_chart.png', dpi=100)
    pieplt.clf()