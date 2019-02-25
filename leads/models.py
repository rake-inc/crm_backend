from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField
from django.conf import settings
from leads.tasks import set_appointment, remind_and_notify
from datetime import datetime
import uuid

User = settings.AUTH_USER_MODEL


# Create your models here.

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1)
    comment = models.TextField(null=False)
    time_stamp = models.DateTimeField(null=False)

    @property
    def fields(self):
        return [field.name for field in self._meta.fields]


class Lead(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    source = models.TextField(null=False)
    company_name = models.TextField(null=False)
    emails = ArrayField(models.EmailField(max_length=64), blank=False, null=False)
    phone_numbers = ArrayField(models.CharField(max_length=10), blank=False, null=False)
    status = models.CharField(
        max_length=5,
        choices=(('hot', 'Hot'), ('warm', 'Warm'), ('Cold', 'cold')),
        null=True
    )
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    appointment = models.DateTimeField(null=True)
    assigned_by = models.ForeignKey(User, related_name='lead_assigned_to')
    assigned_to = models.ForeignKey(User, related_name='lead_assigned_by')

    class Meta:
        indexes = [models.Index(['company_name', 'emails', 'assigned_by', 'assigned_to', 'phone_numbers'])]

    def save(self, *args, **kwargs):
        super(Lead, self).save(*args, **kwargs)
        countdown_seconds = abs(datetime.now() - self.appointment).seconds
        kwargs['cache_obj'] = self
        set_appointment.apply_async(countdown=countdown_seconds, **kwargs)

    @property
    def fields(self):
        return [field.name for field in self._meta.fields]

    def __str__(self):
        return self.company_name


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1)
    customer_name = models.TextField(null=False)
    emails = ArrayField(models.EmailField(max_length=64), blank=False, null=False)
    phone_numbers = ArrayField(models.CharField(max_length=10), blank=True, null=False)
    status = models.CharField(
        max_length=5,
        choices=(('hot', 'Hot'), ('warm', 'Warm'), ('Cold', 'cold')),
        null=True
    )
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    appointment = models.DateTimeField(null=True)
    assigned_by = models.ForeignKey(User, related_name='customer_assigned_to')
    assigned_to = models.ForeignKey(User, related_name='customer_assigned_by')

    class Meta:
        indexes = [models.Index(['customer_name', 'emails', 'assigned_by', 'assigned_to', 'phone_numbers'])]

    def save(self, *args, **kwargs):
        super(Customer, self).save(*args, **kwargs)
        countdown_seconds = abs(datetime.now() - self.appointment).seconds
        kwargs['cache_obj'] = self
        set_appointment.apply_async(countdown=countdown_seconds, **kwargs)

    @property
    def fields(self):
        return [field.name for field in self._meta.fields]


class Reminders(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1)
    message = models.TextField(null=False)
    time_stamp = models.DateTimeField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        print("save overridden")
        super(Reminders, self).save(*args, **kwargs)
        countdown_seconds = abs(datetime.now() - self.time_stamp).seconds
        kwargs['cache_obj'] = self
        remind_and_notify.apply_async(countdown=countdown_seconds, **kwargs)

    @property
    def fields(self):
        return [field.name for field in self._meta.fields]


class Deal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1)
    transaction_id = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='deal_owner')
    transaction_type = models.TextField()
    details = JSONField(verbose_name='transaction_details')

    def save(self, *args, **kwargs):
        super(Deal, self).save(*args, **kwargs)

    @property
    def fields(self):
        return [field.name for field in self._meta.fields]
