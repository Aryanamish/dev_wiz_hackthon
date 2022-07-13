from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=20)
    content = models.TextField()
    cover_photo = models.ImageField(upload_to='media/')
    date_posted = models.DateTimeField(default=timezone.now)