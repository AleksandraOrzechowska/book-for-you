from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ContestForm
from .models import Contest

def add_contest(request):
  if request.method == 'POST':
    form = ContestForm(request.POST)

    if form.is_valid():
      contest = Contest(title=form.cleaned_data['title'],description=form.cleaned_data['description'])
      contest.save()
      return HttpResponseRedirect("/contest-added")

  else:
    form = ContestForm()

  return render(request, "contest/add_contest.html", {
    "form": form
  })


def contest_added(request):
  return render(request, "contest/contest_added.html")


def contests(request):
    return render(request, "contests.html")