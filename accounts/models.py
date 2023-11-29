from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


# class User(AbstractUser):
#     phone = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)
#     avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

#     def __str__(self) -> str:
#         return self.username