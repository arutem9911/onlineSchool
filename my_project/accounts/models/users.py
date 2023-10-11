from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class User(AbstractUser):
    ROLES = [
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student')
    ]

    role = models.CharField(max_length=20, choices=ROLES, default='admin')
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='user', blank=True, null=True, default='user/default-avatar.jpg')
    groups = models.ManyToManyField('accounts.StudyGroup', related_name='users', through='accounts.UserGroup', through_fields=('user', 'group'), blank=True)
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    city = models.CharField(max_length=20, blank=True, null=True, default='')
    phone = models.IntegerField(null=True)


