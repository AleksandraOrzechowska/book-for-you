from django.http.response import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Review

# Create your views here.


def book_review(request, slug):
    review = get_object_or_404(Review,slug=slug)
    return render(request, "reviews/review.html", {"text": review})


def reviews_list(request):
    reviews = Review.objects.all()
    reviews = [review for review in reviews]
    return render(request, "reviews/review_list.html", {
        "reviews": reviews
    }
    )
