
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sport', views.sport, name='sport'),
    path('cse', views.cse, name='cse'),
    path('schools', views.schools, name='schools'),
    path('movie', views.movie, name='movie'),
    path('checkcr', views.checkcr, name='checkcr'),
    path('checkcss', views.checkcss, name='checkcss'),
    path('checksc', views.checksc, name='checksc'),
    path('checkmv', views.checkmv, name='checkmv'),
]
