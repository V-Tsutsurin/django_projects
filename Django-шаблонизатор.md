# Полное руководство по Django-шаблонизатору

## Основы Django-шаблонизатора
Django-шаблонизатор позволяет генерировать HTML с использованием переменных, условий и циклов. Он поддерживает фильтры, теги и работу с контекстом.

---

## Подключение шаблонов в проекте
1. **Настройка в `settings.py`**:
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
- **`DIRS`**: Список директорий, где ищутся шаблоны.
- **`APP_DIRS`**: Если `True`, Django ищет шаблоны в папке `templates` каждого приложения.

2. **Создание папки для шаблонов**:
   - Общие шаблоны: `project_root/templates/`
   - Шаблоны для приложения: `app_name/templates/app_name/`

---

## Основные конструкции шаблонов

### 1. Вывод переменных
```html
<p>{{ переменная }}</p>
```
Если переменная отсутствует, ничего не отобразится (по умолчанию).

### 2. Фильтры
Фильтры изменяют значение переменной:
```html
<p>{{ имя|lower }}</p> <!-- Преобразование в нижний регистр -->
<p>{{ дата|date:"d M Y" }}</p> <!-- Форматирование даты -->
```
**Полный список фильтров:**
- `lower`, `upper`, `title`, `length`, `truncatechars`.
- `date`, `time`, `default`, `yesno`, `escape`.

### 3. Условные конструкции
```html
{% if переменная %}
    <p>Условие выполнено</p>
{% else %}
    <p>Условие не выполнено</p>
{% endif %}
```

### 4. Циклы
```html
<ul>
    {% for item in список %}
        <li>{{ item }}</li>
    {% endfor %}
</ul>
```

Цикловые переменные:
- `forloop.counter` - Счётчик (начинается с 1).
- `forloop.first` - True для первой итерации.
- `forloop.last` - True для последней итерации.

### 5. Комментарии
```html
{# Это комментарий, который не будет виден в HTML #}
```

---

## Теги шаблонизатора

### 1. Подключение другого шаблона
```html
{% include "header.html" %}
```

### 2. Расширение шаблона
Шаблоны могут наследоваться друг от друга:
```html
<!-- base.html -->
<html>
<head>
    <title>{% block title %}Заголовок{% endblock %}</title>
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```
```html
<!-- child.html -->
{% extends "base.html" %}

{% block title %}Дочерний заголовок{% endblock %}

{% block content %}
    <p>Контент дочернего шаблона</p>
{% endblock %}
```

### 3. Работа со статическими файлами
```html
{% load static %}
<img src="{% static 'images/logo.png' %}" alt="Логотип">
```

### 4. Работа с URL-адресами
```html
<a href="{% url 'имя_пути' %}">Ссылка</a>
```

### 5. Переменные и их значение по умолчанию
```html
{{ переменная|default:"Значение по умолчанию" }}
```

---

## Пользовательские фильтры и теги

### Создание пользовательского фильтра
1. Создайте файл `templatetags/my_filters.py`:
```python
from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg
```

2. Использование:
```html
{% load my_filters %}
<p>{{ число|multiply:5 }}</p>
```

### Создание пользовательского тега
1. Создайте тег в том же файле:
```python
@register.simple_tag
def current_time(format_string):
    from datetime import datetime
    return datetime.now().strftime(format_string)
```

2. Использование:
```html
{% load my_filters %}
<p>{% current_time "%H:%M:%S" %}</p>
```

---

## Работа с формами в шаблонах
Django автоматически генерирует HTML для форм:
```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Отправить</button>
</form>
```

### Ручная отрисовка полей формы
```html
<form method="post">
    {% csrf_token %}
    {{ form.username.label_tag }} {{ form.username }}
    {{ form.password.label_tag }} {{ form.password }}
    <button type="submit">Войти</button>
</form>
```

---

## Отладка шаблонов

1. **Вывод отладочной информации**:
```html
{{ debug }}
```

2. **Включение ошибки при использовании несуществующих переменных**:
```python
TEMPLATES = [
    {
        ...
        'OPTIONS': {
            'string_if_invalid': 'НЕИЗВЕСТНО: %s',
        },
    },
]
```

###


## Базовые теги и операторы

### {% extends %}
```django
{% extends "base.html" %}
```
Используется для наследования шаблонов. Указывает, что текущий шаблон расширяет базовый шаблон.

### {% block %}
```django
{% block content %}
    <h1>Содержимое страницы</h1>
{% endblock %}
```
Определяет блок содержимого, который может быть переопределен в дочерних шаблонах.

### {% include %}
```django
{% include "header.html" %}
```
Включает содержимое другого шаблона в текущий шаблон.

### {% csrf_token %}
```django
<form method="post">
    {% csrf_token %}
    <!-- содержимое формы -->
</form>
```
Добавляет CSRF-токен для защиты форм от межсайтовой подделки запросов.

## Условия и циклы

### {% if %}
```django
{% if user.is_authenticated %}
    <p>Привет, {{ user.username }}!</p>
{% else %}
    <p>Пожалуйста, войдите</p>
{% endif %}
```
Условный оператор для проверки условий.

### {% for %}
```django
{% for item in items %}
    <li>{{ item.name }}</li>
{% empty %}
    <li>Список пуст</li>
{% endfor %}
```
Цикл для итерации по последовательностям.

## Фильтры

### {{ value|default:"nothing" }}
```django
<p>Автор: {{ post.author|default:"Аноним" }}</p>
```
Устанавливает значение по умолчанию, если переменная пуста.

### {{ text|linebreaks }}
```django
{{ post.content|linebreaks }}
```
Конвертирует переводы строк в HTML-теги <p> и <br>.

### {{ string|length }}
```django
<p>Длина текста: {{ text|length }}</p>
```
Возвращает длину строки или количество элементов в списке.

## Комментарии

### {# #} - однострочный комментарий
```django
{# Это однострочный комментарий #}
```
Используется для коротких комментариев в одну строку.

### {% comment %} - многострочный комментарий
```django
{% comment %}
    Это многострочный комментарий
    Может содержать несколько строк
{% endcomment %}
```
Используется для многострочных комментариев.

## Работа с формами

### Доступ к данным POST-запроса
```django
{{ request.POST.field_name }}
```
Получение данных, отправленных через POST-запрос.

### Пример формы с обработкой данных
```django
<form method="post">
    {% csrf_token %}
    <input type="text" name="username">
    {% if request.POST %}
        <p>Вы ввели: {{ request.POST.username }}</p>
    {% endif %}
</form>
```
Показывает как получить доступ к отправленным данным формы.

## Вложенные шаблоны и наследование

### Базовый шаблон (base.html)
```django
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Default Title{% endblock %}</title>
</head>
<body>
    {% block content %}
    {% endblock %}
</body>
</html>
```

### Дочерний шаблон
```django
{% extends "base.html" %}

{% block title %}
    Моя страница
{% endblock %}

{% block content %}
    <h1>Моё содержимое</h1>
{% endblock %}
```
Показывает как правильно использовать наследование шаблонов.
# Полное руководство по фильтрам и модификаторам Django

## Текстовые фильтры

### Преобразование текста
```django
{{ value|lower }}  {# преобразует текст в нижний регистр #}
{{ value|upper }}  {# преобразует текст в верхний регистр #}
{{ value|title }}  {# делает первые буквы каждого слова заглавными #}
{{ value|capfirst }}  {# делает первую букву строки заглавной #}
{{ value|truncatewords:2 }}  {# обрезает текст до указанного количества слов #}
{{ value|truncatechars:7 }}  {# обрезает текст до указанного количества символов #}
{{ value|wordcount }}  {# подсчитывает количество слов #}
{{ value|slugify }}  {# преобразует текст в URL-совместимый формат #}
```

### Форматирование текста
```django
{{ value|linebreaks }}  {# преобразует \n в <br> или <p> теги #}
{{ value|linebreaksbr }}  {# преобразует \n только в <br> теги #}
{{ value|safe }}  {# отключает HTML-экранирование #}
{{ value|striptags }}  {# удаляет HTML теги #}
{{ value|escapejs }}  {# экранирует текст для использования в JavaScript #}
{{ value|urlize }}  {# преобразует URL и email-адреса в кликабельные ссылки #}
```

## Числовые фильтры

### Математические операции
```django
{{ value|add:2 }}  {# прибавляет число #}
{{ value|divisibleby:2 }}  {# проверяет делимость на число #}
{{ value|multiply:3 }}  {# умножает на число #}
{{ value|subtract:2 }}  {# вычитает число #}
```

### Форматирование чисел
```django
{{ value|floatformat:2 }}  {# форматирует число с указанным количеством десятичных знаков #}
{{ value|filesizeformat }}  {# форматирует число как размер файла (например, 1.2 MB) #}
{{ value|intcomma }}  {# добавляет запятые для разделения разрядов #}
{{ value|ordinal }}  {# преобразует число в порядковое числительное #}
```

## Фильтры для работы с датами

### Форматирование дат
```django
{{ value|date:"Y-m-d" }}  {# форматирует дату по указанному шаблону #}
{{ value|time:"H:i" }}  {# форматирует время #}
{{ value|timesince }}  {# показывает время, прошедшее с указанной даты #}
{{ value|timeuntil }}  {# показывает время, оставшееся до указанной даты #}
```

### Модификация дат
```django
{{ value|date:"Y-m-d"|add:"5 days" }}  {# добавляет дни к дате #}
{{ value|date:"SHORT_DATE_FORMAT" }}  {# использует предустановленный формат даты #}
```

## Фильтры для списков и словарей

### Работа со списками
```django
{{ value|first }}  {# возвращает первый элемент #}
{{ value|last }}  {# возвращает последний элемент #}
{{ value|length }}  {# возвращает длину списка #}
{{ value|slice:":2" }}  {# возвращает срез списка #}
{{ value|join:", " }}  {# объединяет элементы списка с разделителем #}
{{ value|random }}  {# возвращает случайный элемент #}
```

### Работа со словарями
```django
{{ value|dictsort:"name" }}  {# сортирует словарь по ключу #}
{{ value|dictsortreversed:"name" }}  {# сортирует словарь по ключу в обратном порядке #}
{{ value|get_item:key }}  {# получает значение по ключу #}
```

## Условные фильтры

### Проверка значений
```django
{{ value|default:"nothing" }}  {# значение по умолчанию, если пусто #}
{{ value|default_if_none:"nothing" }}  {# значение по умолчанию, если None #}
{{ value|yesno:"да,нет,может быть" }}  {# преобразует булево значение в текст #}
```

### Логические операции
```django
{{ value|length|divisibleby:2 }}  {# комбинирование фильтров #}
{% if value|length > 5 %}  {# использование фильтров в условиях #}
```

## Пользовательские фильтры
```python
# В файле templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """Удаляет все значения arg из строки value."""
    return value.replace(arg, '')

# В шаблоне:
{% load custom_filters %}
{{ value|cut:" " }}  {# использование пользовательского фильтра #}
```

## Примеры комплексного использования

### Форматирование блога
```django
{% for post in posts %}
    <article>
        <h2>{{ post.title|title }}</h2>
        <p class="date">{{ post.created_at|date:"F j, Y" }}</p>
        <div class="content">
            {{ post.content|linebreaks|truncatewords:50 }}
        </div>
        <p class="tags">
            {{ post.tags|join:", "|default:"No tags" }}
        </p>
    </article>
{% endfor %}
```

### Обработка пользовательского ввода
```django
<div class="comment">
    <h3>{{ comment.user.username|title }}</h3>
    <p>{{ comment.text|linebreaks|urlize|safe }}</p>
    <small>
        Posted {{ comment.created_at|timesince }} ago
        ({{ comment.word_count|default:"0" }} words)
    </small>
</div>
```

### Работа с числовыми данными
```django
<div class="statistics">
    <p>Views: {{ page.views|intcomma }}</p>
    <p>Storage used: {{ storage_size|filesizeformat }}</p>
    <p>Average rating: {{ rating|floatformat:1 }}/5</p>
    <p>You are the {{ visitor_count|ordinal }} visitor!</p>
</div>
```
