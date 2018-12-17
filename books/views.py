from django_filters import rest_framework as filters
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
    Note: Use a Genre's Trello ID (trello_id) when populating the 'genres' field.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = ( filters.DjangoFilterBackend, )
    filterset_fields = ( 'title', 'trello_id', )

class GenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint to view / edit genres.
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = ( filters.DjangoFilterBackend, )
    filterset_fields = ( 'name', 'trello_id', )