from django.contrib import admin
from .models import Book, Author, Tag

# Register your models here.



class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("title",)}
admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Tag)