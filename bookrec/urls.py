from django.urls import path
from bookrec import views

urlpatterns = [
    path('', views.home),
    path('home', views.home, name='home'), # /BookRecommender/
    path('book_view_multi', views.book_view_multi, name='book_view_multi'),
    path('rec_book_page_view', views.rec_book_page_view, name='rec_book_page_view'),
    path('rec_view', views.rec_view, name='rec_view'),
    path('vis_view', views.vis_view, name='vis_view'),
]