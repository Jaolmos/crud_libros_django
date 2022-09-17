from django.urls import path
from .import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('about-us', views.aboutUs, name='about_us')
]