from books.models import Book
from django.shortcuts import redirect, render

# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect("list_books")
    return render(request, "books/login.html", {'users': users})


def list_albums(request):
    books = Book.objects.all()
    return render(request, "books/list_books.html", {"books": books})