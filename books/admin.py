from django.contrib import admin

from .models import Book

class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_started', 'date_finished')

admin.site.register(Book, BooksAdmin)