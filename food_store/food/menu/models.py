from django.db import models
from django.core.validators import MinValueValidator
from django.utils.text import slugify

class Category(models.Model):
    """Категории меню (например, 'Завтраки', 'Напитки')"""
    name = models.CharField('Название', max_length=100, unique=True)
    slug = models.SlugField('URL', max_length=100, unique=True, blank=True)
    order = models.PositiveIntegerField('Порядок', default=0)
    is_active = models.BooleanField('Активно', default=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['order']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class MenuItem(models.Model):
    """Блюдо/напиток"""
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='items',verbose_name='Категория')
    name = models.CharField('Название', max_length=100)
    slug = models.SlugField('URL', max_length=100, unique=True, blank=True)
    description = models.TextField('Описание', blank=True)
    price = models.DecimalField('Цена',max_digits=8,decimal_places=2,validators=[MinValueValidator(0)])
    image = models.ImageField('Фото', upload_to='menu/', blank=True)
    is_active = models.BooleanField('Активно', default=True)
    created_at = models.DateTimeField('Дата добавления', auto_now_add=True)

    class Meta:
        verbose_name = 'Позиция меню'
        verbose_name_plural = 'Позиции меню'
        ordering = ['category', 'name']

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)