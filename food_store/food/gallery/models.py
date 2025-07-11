from django.db import models
from django.utils.text import slugify

class GalleryCategory(models.Model):
    """Категории для фото (например, 'Интерьер', 'Еда', 'Мероприятия')"""
    name = models.CharField('Название', max_length=100, unique=True)
    slug = models.SlugField('URL', max_length=100, unique=True, blank=True)
    order = models.PositiveIntegerField('Порядок', default=0)
    is_active = models.BooleanField('Активно', default=True)

    class Meta:
        verbose_name = 'Категория галереи'
        verbose_name_plural = 'Категории галереи'
        ordering = ['order']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class GalleryImage(models.Model):
    """Фотография для галереи"""
    category = models.ForeignKey(
        GalleryCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='images',
        verbose_name='Категория'
    )
    title = models.CharField('Название', max_length=200, blank=True)
    image = models.ImageField('Файл', upload_to='gallery/%Y/%m/')
    description = models.TextField('Описание', blank=True)
    is_featured = models.BooleanField('Избранное', default=False)  # Для показа на главной
    created_at = models.DateTimeField('Дата добавления', auto_now_add=True)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['-created_at']

    def __str__(self):
        return self.title if self.title else f"Фото #{self.id}"