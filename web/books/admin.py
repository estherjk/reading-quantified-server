from django.contrib import admin

from .models import Book, Genre

class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_started', 'date_finished')

admin.site.register(Book, BooksAdmin)
admin.site.register(Genre)