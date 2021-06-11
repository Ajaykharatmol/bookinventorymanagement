from django.urls import path

from . import views

from .views import *
   


urlpatterns = [
    path('', views.index, name='index'),
    path('AddBookform', views.AddBookform, name='AddBookform'),
    path('addBook', views.addBook, name='addBook'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
  
    
]