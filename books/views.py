from django.shortcuts import get_object_or_404, render
from .models import Book
from .forms import BookForm
from django.http import Http404

# Create your views here.


def add_book(request):
    return render(request, "books/add_book.html", {})


def start_page(request):
    return render(request, "books/start.html", {})


def books(request):
    all_books = Book.objects.all().order_by("title")
    books_sum = all_books.count()
    return render(request, "books/books.html", {'all_books': all_books, "books_sum": books_sum})


def book_details(request, slug):
    book = get_object_or_404(Book,slug=slug)
    return render(request, "books/book_details.html",{
        "title": book.title,
        "description" : book.description,
    })