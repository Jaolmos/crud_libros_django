from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Eres un gran programador Jose! yo confio en ti! llegaras lejos!! </h1>")

def aboutUs(request):  #Función que nos retorna la pagina html de acerca de nosotros.
    return render(request, 'pages/about_us.html')