from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


def index(request):
    return render(request, 'pages/index.html')

def aboutUs(request):  #Función que nos retorna la pagina html de acerca de nosotros.
    return render(request, 'pages/about_us.html')

def books(request):
    books = Book.objects.all()
    return render(request, 'books/books.html', {'books': books} )

def createBook(request):
    form = BookForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('books')

    return render(request, 'books/create.html', {'form': form})

def editBook(request):
    return render(request, 'books/edit.html') 

def delete(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('books')