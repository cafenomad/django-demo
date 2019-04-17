# -*- coding: utf-8 -*-
"""books.urls."""

from django.urls import re_path
from books.views.book import BookListView
from books.views.book import BookDetailView


urlpatterns = [

    re_path(r'^$',
            BookListView.as_view(),
            name='book_top'),

    re_path(r'^(?P<book_id>\d+)/$',
            BookDetailView.as_view(),
            name='book_detail'),
]
