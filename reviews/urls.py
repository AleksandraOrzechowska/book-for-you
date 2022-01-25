from django.urls import path
from . import views

urlpatterns = [
    path("<slug:slug>",views.book_review, name="book-review"),
    path('', views.reviews_list, name="reviews-list"),


]
