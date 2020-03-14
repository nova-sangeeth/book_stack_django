from django.forms import ModelForm, Form
from .models import Book


class book_form(ModelForm):
    class meta:
        model = Book
        fields = ['name', 'author', 'publisher', 'pages', 'price']
