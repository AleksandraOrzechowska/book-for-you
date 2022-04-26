from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "description",
                  "genre"]

class Book_Form(forms.Form):
    title = forms.CharField(label = "Book Title", max_length=200)
    description = forms.CharField(label="Description",widget=forms.Textarea, max_length=500)