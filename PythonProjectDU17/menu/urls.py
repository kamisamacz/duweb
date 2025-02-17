from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ukol1/', views.ukol1, name='ukol1'),
    path('ukol2/', views.ukol2, name='ukol2'),
    path('ukol3/', views.ukol3, name='ukol3'),
    path('ukol4/', views.ukol4, name='ukol4'),
    path('ukol5/', views.ukol5, name='ukol5'),
    path('vysledky/', views.vysledky, name='vysledky'),
]
