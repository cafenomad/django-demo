# -*- coding: utf-8 -*-
"""app.views.book."""

from datetime import date
from django.views.generic import View
from django.shortcuts import render_to_response
from books.models.book import Book


class BookListView(View):

    """BookListView."""

    def get(self, request):
        """Get."""
        books = Book.objects.all()
        today = date.today()
        return render_to_response(u'book/index.html', {
            u'books': books,
            u'today': today,
        })


class BookDetailView(View):

    """BookDetailView."""

    def get(self, request, book_id):
        """Get."""
        book = Book.objects.get(id=book_id)
        return render_to_response(u'book/detail.html', {
            u'book': book,
        })
