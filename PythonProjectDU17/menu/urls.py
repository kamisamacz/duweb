from django.urls import path
from . import views
from .views import ContactView

urlpatterns = [
    path('', views.home, name='home'),
    path('ukol1/', views.ukol1, name='ukol1'),
    path('ukol2/', views.ukol2, name='ukol2'),
    path('ukol3/', views.feedback_view, name='ukol3'),  # Zkontroluj tento řádek
    path('ukol4/', views.ukol4, name='ukol4'),
    path('ukol5/', ContactView.as_view(), name='ukol5'),
    path('vysledky/', views.vysledky, name='vysledky'),

]
