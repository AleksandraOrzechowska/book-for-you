from django.contrib import admin
from .models import Book, Author, Tag




class BookAdmin(admin.ModelAdmin):
    list_display = ("title",)
    list_filter = ("genre","tags","author",)
    
    prepopulated_fields = {"slug" : ("title",)}
admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Tag)