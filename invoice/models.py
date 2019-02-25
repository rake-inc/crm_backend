from django.db import models


# Create your models here.

class Template(models.Model):
    name = models.TextField(null=False)
    template = models.FileField(upload_to='documents/%Y/%m/%d/')
