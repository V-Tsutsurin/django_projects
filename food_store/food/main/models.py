from django.db import models

# Create your models here.
class Main(models.Model):
    page_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    about = models.TextField()



    def __str__(self):
        return self.name