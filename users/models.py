from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.postgres.fields import ArrayField
from permissions.models import Permission


class UserManager(BaseUserManager):

    def get_by_natural_key(self, email_):
        return self.get(email=email_)

# Create your models here.

class User(AbstractBaseUser):
    id = models.BigIntegerField(primary_key=True, editable=False)
    email = models.EmailField(unique=True, null=False, max_length=32, blank=False)
    is_super_admin = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    first_name = models.TextField(null=False)
    last_name = models.TextField(null=True)
    phone_numbers = ArrayField(models.CharField(max_length=12), blank=True, null=False)
    is_admin = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    username = models.TextField()
    permission = models.ForeignKey(Permission, default=Permission.objects.get(name='default').pk)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'username', 'password', 'phone_numbers']

    class Meta:
        indexes = [models.Index(['username', 'email', 'phone_numbers'])]
        db_table = "users_user"

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        self.id = abs(id(self.email))
        if not self.permission is None:
            self.permission = Permission.objects.get(name='default')
        super(User, self).save(*args, **kwargs)

    def create(self, **kwargs):
        user_data = kwargs['user_data']
        for field, value in user_data.iteritems():
            setattr(self, field, value)
        self.save()

    @property
    def fields(self):
        return [field.name for field in self._meta.fields]
