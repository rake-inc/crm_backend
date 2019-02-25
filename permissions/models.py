from django.db import models
from leads.models import Lead, Deal, Customer
import uuid


# Create your models here.

class Permission(models.Model):
    name = models.TextField(unique=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid1)
    leads = models.BooleanField(default=False)
    deals = models.BooleanField(default=False)
    customers = models.BooleanField(default=False)
    users = models.BooleanField(default=False)

    class Meta:
        db_table = 'permissions_permission'

    def save(self, *args, **kwargs):
        super(Permission, self).save(*args, **kwargs)

    @property
    def fields(self):
        return [field.name for field in self._meta.fields]
