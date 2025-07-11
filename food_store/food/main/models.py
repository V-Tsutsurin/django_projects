from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField  # Для удобного редактирования текста

class Page(models.Model):
    """Статические страницы (О нас, Контакты и т.д.)"""
    PAGE_CHOICES = [
        ('home', 'Главная'),
        ('about', 'О нас'),
        ('contacts', 'Контакты'),
    ]

    page_type = models.CharField('Тип страницы',max_length=20,choices=PAGE_CHOICES,unique=True)
    title = models.CharField('Заголовок', max_length=200)
    slug = models.SlugField('URL', max_length=100, unique=True, blank=True)
    content = RichTextField('Контент', blank=True)
    seo_title = models.CharField('SEO Title', max_length=200, blank=True)
    seo_description = models.TextField('SEO Description', blank=True)
    is_active = models.BooleanField('Активно', default=True)

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    def __str__(self):
        return self.get_page_type_display()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.page_type)
        super().save(*args, **kwargs)


class Contact(models.Model):
    """Контакты кафе (адрес, телефон, email)"""
    CONTACT_TYPE_CHOICES = [
        ('address', 'Адрес'),
        ('phone', 'Телефон'),
        ('email', 'Email'),
        ('social', 'Соцсеть'),
    ]

    type = models.CharField('Тип', max_length=20, choices=CONTACT_TYPE_CHOICES)
    value = models.CharField('Значение', max_length=200)
    icon = models.CharField('Иконка (FontAwesome)', max_length=50, blank=True)  # Например, "fa-map-marker"
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ['order']

    def __str__(self):
        return f"{self.get_type_display()}: {self.value}"


class Promotion(models.Model):
    """Акции и спецпредложения"""
    title = models.CharField('Название', max_length=200)
    slug = models.SlugField('URL', max_length=200, unique=True, blank=True)
    short_description = models.CharField('Краткое описание', max_length=300)
    content = RichTextField('Подробности', blank=True)
    image = models.ImageField('Изображение', upload_to='promotions/')
    start_date = models.DateField('Дата начала')
    end_date = models.DateField('Дата окончания')
    is_active = models.BooleanField('Активно', default=True)

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'
        ordering = ['-start_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Event(models.Model):
    """Мероприятия в кафе (концерты, мастер-классы)"""
    title = models.CharField('Название', max_length=200)
    slug = models.SlugField('URL', max_length=200, unique=True, blank=True)
    description = RichTextField('Описание')
    image = models.ImageField('Постер', upload_to='events/')
    date = models.DateTimeField('Дата и время')
    price = models.DecimalField(
        'Цена',
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        blank=True,
        null=True
    )
    registration_required = models.BooleanField('Нужна регистрация', default=False)
    max_attendees = models.PositiveIntegerField('Макс. участников', blank=True, null=True)

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
        ordering = ['-date']

    def __str__(self):
        return f"{self.title} ({self.date.strftime('%d.%m.%Y')})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)