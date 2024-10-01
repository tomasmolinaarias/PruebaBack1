from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('experiencia/', views.experience, name='experiencia'), 
    path('contact/', views.contact, name='contact'),
]
