from django.core import validators
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from books.models import Book
from django.core.validators import MinLengthValidator


class Review(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(validators=[MinLengthValidator(15)])
    book = models.ForeignKey(Book, on_delete=models.CASCADE,null=True, related_name="book")
    date = models.DateField(auto_now=True)
    slug = models.SlugField(default="",blank=True,null=False,db_index=True)


    def get_absolute_url(self):
        return reverse("book-review", args=[self.slug])

    def __str__(self):
        return self.title
