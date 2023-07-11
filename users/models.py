from django.db import models


from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=30, unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=20, verbose_name='телефон', blank=True, null=True)
    city = models.CharField(max_length=30, verbose_name='город', blank=True, null=True)
    avatar = models.ImageField(upload_to='users', verbose_name='аватар', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []