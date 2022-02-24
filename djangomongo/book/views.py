from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    books = Book.objects.all()
    paginator = Paginator(books,2)

    page_number = request.GET.get('page')
    books_page = paginator.get_page(page_number)
    return render(request, 'book/index.html',{'books':books_page})
