from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    description = models.CharField(max_length=800)

    def name(self):
        return f"{self.first_name} {self.second_name}"

    def __str__(self):
        return self.name()

class Tag(models.Model):
    text = models.CharField(max_length=30)

    def __str__(self):
        return self.text

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=800)
    author = models.ManyToManyField(Author)
    genre = models.CharField(max_length=30,blank=True)
    slug = models.SlugField(default="",blank=True,null=False,db_index=True)
    tags = models.ManyToManyField(Tag)
    
    def get_absolute_url(self):
        return reverse("book-details", args=[self.slug])
    

    def __str__(self):
        return self.title
