from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from books.models import Tag

class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=800)
    slug = models.SlugField(default="",blank=True,null=False,db_index=True)
    tags = models.ManyToManyField(Tag)
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='news/',default="")

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'

def __str__(self):
    return self.title
