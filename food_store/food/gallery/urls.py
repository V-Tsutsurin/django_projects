from django.urls import path
from gallery import views

app_name = 'gallery'

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('about/', views.about, name='about'),
]