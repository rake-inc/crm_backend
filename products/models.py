from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField


# Create your models here.
class Category(models.Model):
    name = models.TextField(null=False, unique=True)
    products = ArrayField(models.ForeignKey('Product', on_delete=models.CASCADE))

    class Meta:
        indexes = [models.Index(['name'])]


class Product(models.Model):
    name = models.TextField(null=False)
    description = models.TextField(null=False)
    link = models.URLField(max_length=16, null=False)
    prices = ArrayField(JSONField(), blank=False)
    category = models.ForeignKey(Category)
    company_name = models.ForeignKey('Company')

    class Meta:
        indexes = [models.Index(['name', 'link'])]


class Company(models.Model):
    name = models.TextField(null=False)
    products = ArrayField(models.ForeignKey(Product, on_delete=models.CASCADE), blank=False)

    class Meta:
        indexes = [models.Index(['name'])]
