from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pages/index.html')

def aboutUs(request):  #Función que nos retorna la pagina html de acerca de nosotros.
    return render(request, 'pages/about_us.html')

def books(request):
    return render(request, 'books/books.html')

def createBook(request):
    return render(request, 'books/create.html')

def editBook(request):
    return render(request, 'books/edit.html')