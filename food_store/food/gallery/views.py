from django.shortcuts import render
from .models import GalleryImage

# Create your views here.
def gallery(request):
    featured_images = GalleryImage.objects.filter(is_featured=True)

    # Получить фото из категории "Интерьер" с тегом "лето"
    summer_interior = GalleryImage.objects.filter(
        category__name='Интерьер',
        tags__tag__name='лето'
    ).select_related('category')

def about(request):
    pass