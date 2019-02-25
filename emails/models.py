from django.db import models
from django.contrib.postgres.fields import ArrayField
from users.models import User


# Create your models here.

class Content(models.Model):
    description = models.TextField()


class Email(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    emails = ArrayField(models.EmailField(max_length=32, blank=False))
    time = models.TimeField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
