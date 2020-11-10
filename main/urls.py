from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='index'),
    path('ticket/', views.ticket, name='ticket'),
    path('about/', views.index, name='about'),
    path('contacts/', views.index, name='contacts'),
    path('reviews/', views.reviews, name='reviews'),
]