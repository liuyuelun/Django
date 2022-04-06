from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import Book
def all_book(request):
    all_book = Book.objects.all()
    return render(request,"bookstore/all_book.html",locals())

def update_book(request,book_id):
    try:
        book=Book.objects.get(id=book_id)
    except Exception as e:
        print("--update book error is %s"%(e))
        return HttpResponse("--the book is not existed--")

    if request.method == "GET":
        return render(request,"bookstore/update_book.html",locals())
    elif request.method == "POST":
        price = request.POST["price"]
        market_price = request.POST["market_price"]
        book.price = price
        book.market_price=market_price
        book.save()
        return HttpResponseRedirect("/bookstore/all_book")