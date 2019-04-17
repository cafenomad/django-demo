# -*- coding: utf-8 -*-
"""app.models.book."""


from django.db import models


class Book(models.Model):

    """ Book """

    title = models.CharField(
        u'Book Title',
        default=u'',
        max_length=128,
        blank=False,
        help_text=u'')

    price = models.IntegerField(
        u'Book Price',
        default=u'',
        blank=False,
        help_text=u'')

    memo = models.TextField(
        u'Book Memo',
        default=u'',
        blank=True,
        help_text=u'')

    created = models.DateTimeField(
        u'Created Time',
        auto_now=True,
        help_text=u'')

    updated = models.DateTimeField(
        u'Updated Time',
        auto_now=True,
        help_text=u'')
