from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book
from .forms import book_form


# def views(request):
#     return render(request, 'index.html')


# class booklist(ListView):
#     model = Book


# class bookview(DetailView):
#     model = Book


# class bookcreate(CreateView):
#     model = Book
#     fields = ['name', 'author', 'publisher', 'pages', 'price']


# class bookupdate(UpdateView):
#     model = Book
#     fields = ['name', 'author', 'publisher', 'pages', 'price']
#     success_url = reverse_lazy('book_list')


# class bookdelete(DeleteView):
#     model = Book
#     success_url = reverse_lazy('book_list')

# FUNCTION BASED VIEWS.

def booklist(request):
    book = Book.objects.all()
    data = {}
    data['object_list'] = book
    return render(request, 'book_list.html', data)


def bookview(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "book_view.html", {'object': book})


def bookcreate(request):
    form = book_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('booklist')
    return render(request, "book_form.html", {'form': form})


def bookupdate(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = book_form(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('booklist')
    return render(request, 'book_form.html', {"form": form})


def bookdelete(requst):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('booklist')
    return render(request, "book_delete.html", {"object": book})
