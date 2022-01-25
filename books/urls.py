from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_page,name="start-page"),
    path("add_book", views.add_book, name="add-book"),
    path("books", views.books),
    path("books/<slug:slug>",views.book_details, name="book-details"),

]
