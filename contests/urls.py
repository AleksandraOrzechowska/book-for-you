from django.urls import path
from . import views

urlpatterns = [
    path("add_contest", views.add_contest, name="add-contest"),
    path("contests", views.contests),
    path("contest_added",views.contest_added,name="contest-added"),
]