from django.urls import path
from .import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('about-us', views.aboutUs, name='about_us'),
    path('books', views.books, name='books'),
    path('create-book', views.createBook, name='create_book'),
    path('edi-book', views.editBook, name='edit_book')
    
]

