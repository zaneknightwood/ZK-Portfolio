# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 12:40:58 2023

@author: Zane Knightwood
"""

# Creates the book class for storing book information. Also sets up a function to ensure an object is of the book type.

class Book:
    #constructor
    def __init__(self, ind, a, g, i, l, p, r, t, c):
        self.bookId = ind
        self.author = a
        self.genre = g
        self.img = i
        self.link = l
        self.pages = p
        self.rating = r
        self.title = t
        self.percent_match = c
        
    
# Sets book data based on a list.
def setBookData(ind, bookList):
    bookId = int(ind)
    author = bookList[0]
    genre = bookList[1]
    img = bookList[2]
    link = bookList[3]
    pages = bookList[4]
    rating = bookList[5]
    title = bookList[6]
    percent_match = bookList[7]
        
    book = Book(bookId, author, genre, img, link, pages, rating, title, percent_match)
    
    return book

# A function to check if an object is of the book type.
def is_book(thing):
    if isinstance(thing, Book):
        return True
    else: return False