from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse
from urllib.parse import urlencode
from bookrec import book, bookSorting, pieChart, stackedBar

def home(request):
    try:
        if request.method == 'POST':
            book_title = request.POST['user_title']
            if book_title == '':
                return render(request, 'bookrec/home.html', {
                    'no_book': True
                })
            else:
                user_book = bookSorting.get_book(book_title)
                if user_book == False:
                    return render(request, 'bookrec/home.html', {
                    'no_book': True
                })
                if book.is_book(user_book):
                    base_url = reverse('rec_view')
                    query_string = urlencode({'book': user_book.bookId})
                    url = '{}?{}'.format(base_url, query_string)
                    return redirect(url)
                else:
                    base_url = reverse('book_view_multi')
                    query_string = urlencode({'book': book_title})
                    url = '{}?{}'.format(base_url, query_string)
                    return redirect(url)
        return render(request, 'bookrec/home.html', {
            'no_book': False
        })
    except:
        raise Http404()

def book_view_multi(request):
    try:
        if request.method == 'POST':
            book_index = request.POST.get('book_title_combo')
            base_url = reverse('rec_view')
            query_string = urlencode({'book': book_index})
            url = '{}?{}'.format(base_url, query_string)
            return redirect(url)
        book_title = request.GET.get('book')
        user_books = bookSorting.get_book(book_title)
        num_books = len(user_books)
        books = []
        for book in user_books:
            books.append([book.title, book.bookId])
        return render(request, 'bookrec/book_view_multi.html', {
            'num_books': num_books,
            'books': books
        })
    except:
        raise Http404()

def rec_book_page_view(request):
    try:
        book_data = request.GET.get('book')
        book_data = book_data.split(',')
        book_id = book_data[0]
        percent = book_data[1]
        rec_book = bookSorting.get_book_byID(book_id, percent)
        book_title = rec_book.title
        book_img = rec_book.img
        author_list = rec_book.author
        author_list = author_list.split(',')
        genre_list = rec_book.genre
        genre_list = genre_list.split(',')
        rating = rec_book.rating
        perc_match = rec_book.percent_match
        book_link = rec_book.link
        return render(request, 'bookrec/rec_book_page_view.html', {
            'book_title': book_title,
            'book_img': book_img,
            'author_list': author_list,
            'genre_list': genre_list,
            'rating': rating,
            'perc_match': perc_match,
            'book_link': book_link,
        })
    except:
        raise Http404()
    
def rec_view(request):
    try:
        book_index = request.GET.get('book')
        user_book = bookSorting.get_book_byID(book_index)
        books = bookSorting.get_recommended_books(user_book)
        book_urls = []
        for book in books:
            book_param = str(book.bookId) + ',' + str(book.percent_match)
            base_url = reverse('rec_book_page_view')
            query_string = urlencode({'book': book_param})
            url = '{}?{}'.format(base_url, query_string)
            book_urls.append(url)
        vis_base = reverse('vis_view')
        query_string = urlencode({'book': book_index})
        vis_url = '{}?{}'.format(vis_base, query_string)
        return render(request, 'bookrec/rec_view.html',{
            'book1_title': books[0].title,
            'book1_img': books[0].img,
            'book1_url': book_urls[0],
            'book2_title': books[1].title,
            'book2_img': books[1].img,
            'book2_url': book_urls[1],
            'book3_title': books[2].title,
            'book3_img': books[2].img,
            'book3_url': book_urls[2],
            'book4_title': books[3].title,
            'book4_img': books[3].img,
            'book4_url': book_urls[3],
            'book5_title': books[4].title,
            'book5_img': books[4].img,
            'book5_url': book_urls[4],
            'book6_title': books[5].title,
            'book6_img': books[5].img,
            'book6_url': book_urls[5],
            'vis_url': vis_url,
        }) 
    except:
        raise Http404()
    
def vis_view(request):
    book_index = request.GET.get('book')
    user_book = bookSorting.get_book_byID(book_index)
    pieChart.make_pie(user_book)
    stackedBar.make_bar(user_book)
    model_explanation = 'https://www.pythonanywhere.com/user/zaneknightwood/files/home/zaneknightwood/model_explanation.png'
    return render(request, 'bookrec/vis_view.html', {
        'model_explanation': model_explanation
    })



