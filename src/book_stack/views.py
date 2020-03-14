from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book


class booklist(ListView):
    model = Book


class bookview(DetailView):
    model = Book


class bookcreate(CreateView):
    model = Book
    fields = ['name', 'author', 'publisher', 'pages', 'price']


class bookupdate(UpdateView):
    model = Book
    fields = ['name', 'author', 'publisher', 'pages', 'price']
    success_url = reverse_lazy('book_list')


class bookdelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')
