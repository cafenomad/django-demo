# -*- coding: utf-8 -*-
"""app.admin."""


from django.contrib import admin
from books.models.book import Book


class BookAdmin(admin.ModelAdmin):

    """BookAdmin."""

    search_fields = ('title',
                     'price',
                     'memo',)

    list_display = ('title',
                    'price',
                    'created',
                    'updated',)

    ordering = ('updated',)


admin.site.register(Book, BookAdmin)
