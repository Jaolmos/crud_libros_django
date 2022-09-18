from django.shortcuts import render
from .models import Book


def index(request):
    return render(request, 'pages/index.html')

def aboutUs(request):  #Función que nos retorna la pagina html de acerca de nosotros.
    return render(request, 'pages/about_us.html')

def books(request):
    books = Book.objects.all()
    return render(request, 'books/books.html', {'books': books} )

def createBook(request):
    return render(request, 'books/create.html')

def editBook(request):
    return render(request, 'books/edit.html') 