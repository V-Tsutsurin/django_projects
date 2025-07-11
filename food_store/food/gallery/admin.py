from django.contrib import admin
from .models import GalleryCategory, GalleryImage

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_featured')
    list_filter = ('category', 'is_featured')
    search_fields = ('title', 'description')

admin.site.register(GalleryCategory)

