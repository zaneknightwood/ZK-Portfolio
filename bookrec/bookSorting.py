"""
Created on Thu Nov 30 17:06:16 2023

@author: Zane Knightwood
"""

# Contains the necessary functions to collect a set of 6 recommended books based on user input. 

from bookrec import dataProcessing
from collections import Counter
from bookrec import book

# Takes in a book title and compares it to all books in dataframe.
# Returns a list with 6 book recommendations based on matching author, genre, rating, and number of pages.
def get_recommended_books(user_book):
    # gets the dataframe from dataProcessing
    df = dataProcessing.getDF()
    user_index = user_book.bookId
    user_author = user_book.author.split(',')
    user_genre = user_book.genre.split(',')
    user_pages = user_book.pages
    user_rating = user_book.rating

    # set up necessary variables
    matching_books = []
    book_recommendations = []
    criteria_count = len(user_author) + len(user_genre) + 2

    # search through database for book whose authors are the same as input book and add thier index to matching_books
    for i in user_author:
        matching_books.append(df.index[df['author'].str.contains(i)].tolist())
        
    # search through database for book whose genres are the same as input book and add thier index to matching_books
    for i in user_genre:
        matching_books.append(df.index[df['genre'].str.contains(i)].tolist())

    # search through database for book whose number of pages and ratings are the same as input book and add thier index to matching_books
    matching_books.append(df.index[df['pages']==user_pages].tolist())
    matching_books.append(df.index[df['rating']==user_rating].tolist())

    # flatten out the list
    matching_books = [j for sub in matching_books for j in sub]

    # count the number of instances of each index in the list, return a list of tuples where (index, number of instances)
    most_common_books = Counter(matching_books).most_common(7)

    # using the index, create a new book type from the dataframe row and add it to the list of recommendations until 7 books present
    for i in most_common_books:
        percent_match = i[1] / criteria_count
        percent_match = round(percent_match, 2)
        percent_match = percent_match * 100
        if len(book_recommendations) < 6 and user_index != i[0]:
            book_data = df.loc[i[0]].tolist()
            book_data.append(int(percent_match))
            book1 = book.setBookData(i[0], book_data)
            book_recommendations.append(book1)
    
    return book_recommendations

# Searches the dataframe for a book matching the title and returns the matching book.
# If more than one matching book is found, returns a list of those books.
def get_book(title):
    # gets the dataframe from dataProcessing
    df = dataProcessing.getDF()

    # searches the dataframe for any matching title and adds the index to a list
    title_index = df.index[df['title'].str.contains(title, case=False)].tolist()
    book_list = []
    
    # checks the title_index list for length
    # returns single book if only one entry, list of books if more than one, with percents added
    # returns false if list is empty
    if len(title_index) == 0:
        return False
    elif len(title_index) == 1:
        index = title_index[0]
        percent = 100
        book_data = df.loc[index].tolist()
        book_data.append(percent)
        user_book = book.setBookData(index, book_data)
        
        return user_book
    else:
        for i in range(len(title_index)):
            index = title_index[i]
            percent = 100
            book_data = df.loc[index].tolist()
            book_data.append(percent)
            book_list.append(book.setBookData(index, book_data))
        print(f'found {i}')
        return book_list

# Searches the dataframe for a book matching the index and returns the matching book with the percent added.
def get_book_byID(index, percent=100):
    df = dataProcessing.getDF()
    index = int(index)
    book_data = df.loc[index].tolist()
    book_data.append(percent)
    user_book = book.setBookData(index, book_data)
    return user_book

# Takes in a book and compares it to all books in dataframe.
# Returns a list with 6 book recommendations based on matching author, genre, rating, and number of pages.
# Also returns a list with the collected data used to make the determination.
def get_book_rec_augepara(user_book):
    df = dataProcessing.getDF()
    matching_books = []
    book_recommendations = []
    author_match = []
    genre_match = []
    rating_match = []
    pages_match = []
    au_ge_pa_ra = []
    user_author = user_book.author.split(',')
    user_genre = user_book.genre.split(',')
    criteria_count = len(user_author) + len(user_genre) + 2

    # search through database for book whose authors are the same as input book and add thier index to matching_books
    for i in user_author:
        author_match.append(df.index[df['author'].str.contains(i)].tolist())
    
        
    # search through database for book whose genres are the same as input book and add thier index to matching_books
    for i in user_genre:
        genre_match.append(df.index[df['genre'].str.contains(i)].tolist())

    # search through database for book whose number of pages and ratings are the same as input book and add thier index to matching_books
    pages_match.append(df.index[df['pages']==user_book.pages].tolist())
    rating_match.append(df.index[df['rating']==user_book.rating].tolist())

    # flatten out the list
    author_match = [j for sub in author_match for j in sub]
    genre_match = [j for sub in genre_match for j in sub]
    pages_match = [j for sub in pages_match for j in sub]
    rating_match = [j for sub in rating_match for j in sub]
    
    matching_books = author_match + genre_match + pages_match + rating_match

    # count the number of instances of each index in the list, return a list of tuples where (index, number of instances)
    author_match = Counter(author_match).most_common()
    genre_match = Counter(genre_match).most_common()
    pages_match = Counter(pages_match).most_common()
    rating_match = Counter(rating_match).most_common()

    
    most_common_books = Counter(matching_books).most_common(7)

    # using the index, create a new book type from the dataframe row and add it to the list of recommendations until 7 books present
    for i in most_common_books:
        percent_match = i[1] / criteria_count
        percent_match = round(percent_match, 2)
        if user_book.bookId != i[0]:
            book_data = df.loc[i[0]].tolist()
            book_data.append(percent_match)
            book1 = book.setBookData(i[0], book_data)
            book_recommendations.append(book1)
            
    # takes the matching elements found above for each book in book_recommendations and adds them to a list
    for i in book_recommendations:
        for j in author_match:
            if i.bookId == j[0]:
                au_ge_pa_ra.append((i.bookId,'au',j[1]))
        for k in genre_match:
            if i.bookId == k[0]:
                au_ge_pa_ra.append((i.bookId, 'ge',k[1]))
        for l in pages_match:
            if i.bookId == l[0]:
                au_ge_pa_ra.append((i.bookId, 'pa',l[1]))
        for m in rating_match:
            if i.bookId == m[0]:
                au_ge_pa_ra.append((i.bookId, 'ra',m[1]))
    
    return [book_recommendations, au_ge_pa_ra]
        