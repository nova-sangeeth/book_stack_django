from django.forms import ModelForm, Form
from .models import Book


class book_form(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
