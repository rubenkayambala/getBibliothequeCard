from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('register/', views.RegisterView, name='register'),
    path('list/', views.ListView, name='list'),
    path('detail/<id>', views.DetailView, name='detail'),
    path('carte/<id>', views.CarteView, name='carte'),
    path('pdf/', views.pdf, name='pdf'),
]