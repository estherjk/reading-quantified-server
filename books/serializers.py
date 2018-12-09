from rest_framework import serializers

from .models import Book, Genre

class BookSerializer(serializers.HyperlinkedModelSerializer):
    # Instead of showing the genre hyperlinks, show the names
    # https://www.django-rest-framework.org/api-guide/relations/#slugrelatedfield
    genres = serializers.SlugRelatedField(
        many=True,
        queryset=Genre.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Book
        fields = '__all__'

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'