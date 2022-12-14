from django.urls import path
from .import views
from django.conf import settings
from django.contrib.staticfiles.urls import static 

urlpatterns = [
    path('', views.index, name='index'),
    path('about-us', views.aboutUs, name='about_us'),
    path('books', views.books, name='books'),
    path('create-book', views.createBook, name='create_book'),
    path('edit-book/<int:id>', views.editBook, name='edit_book'),
    path('delete-book/<int:id>', views.delete, name='delete_book')
    
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

