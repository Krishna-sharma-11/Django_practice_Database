from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Book
from django.db.models import Avg, Min  # Max, min also


# Create your views here.
def index(request):
    books = Book.objects.all().order_by("-rating") # default ascending and "-title" gives descending order 
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    min_rating = books.aggregate(Min("rating"))

    return render(
        request,
        "book_outlet/index.html",
        {
            "books": books,
            "total_number_of_books": num_books,
            "average_rating": avg_rating,
            "minimum_rating": min_rating,
        },
    )


def book_details(request, slug):
    #   try:
    #       book = Book.objects.get(pk=id)
    #   except:
    #       raise Http404()
    book = get_object_or_404(
        Book, slug=slug
    )  # Right side is name and left side is parameter
    return render(
        request,
        "book_outlet/book_details.html",
        {
            "title": book.title,
            "author": book.author,
            "rating": book.rating,
            "is_bestseller": book.is_bestselling,
        },
    )
