from django.shortcuts import render
from rest_framework import viewsets

from .models import Book, Genre
from .serializers import BookSerializer, GenreSerializer

def index(request):
    """
    View for the books home page.
    """
    return render(request, 'books/index.html')

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint to view / edit books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class GenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint to view / edit genres.
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer