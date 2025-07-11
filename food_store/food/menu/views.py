from django.shortcuts import render
from .models import MenuItem

# Create your views here.
def menu(request):
    pass

def dish(request):
    pass

def drink(request):
    drinks = MenuItem.objects.filter(
        category__name='Напитки',
        is_active=True
    ).select_related('category')

# Получить все активные блюда из категории "Напитки"
