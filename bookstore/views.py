from django.shortcuts import render
from .models import Book
def all_book(request):
    all_book = Book.objects.all()
    return render(request,"bookstore/all_book.html",locals())

# Create your views here.