from django.db import models

# Create your models here.
class Classes(models.Model):
    code = models.CharField(max_length=100)
    title = models.CharField(max_length=100)