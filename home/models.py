from .manager import BaseModel
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Category(BaseModel):
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name

class Tags(BaseModel):
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name

class Social(BaseModel):
    link = models.CharField(max_length=289)
    icon = models.ImageField(upload_to='social/')

    def __str__(self) -> str:
        return self.link

class Contact(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()

class News(BaseModel):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to="news/")
    view_count = models.BigIntegerField(default=0, blank=True, null=True)
    body = RichTextField()
    slug = models.SlugField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tags)

    def __str__(self) -> str: 
        return self.title
    
     # You can have
    def get_absolute_url(self):
         return reverse('new-details', kwargs={"id": self.id})
    
     # An alternative to use to update the view count 
    def update_views(self, *args, **kwargs):
         self.view_count = self.view_count + 1
         super(News, self).save(*args, **kwargs)