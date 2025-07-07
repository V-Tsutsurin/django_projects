from django.urls import path
from menu import views

app_name = 'menu'

urlpatterns = [
    path('', views.menu, name='menu'),
    path('dish/', views.dish, name='dish'),
]