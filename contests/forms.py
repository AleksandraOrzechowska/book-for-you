from django import forms


class ContestForm(forms.Form):
    title = forms.CharField(label="Contest Title", max_length=100)
    description = forms.CharField(label="Description", widget=forms.Textarea, max_length=500)
