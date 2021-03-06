# -*- coding: utf-8 -*-

from django.utils import timezone
from haystack.indexes import SearchIndex, Indexable, CharField, DateTimeField

from .models import Document


class DocumentIndex(SearchIndex, Indexable):
    text = CharField(document=True, use_template=True)
    date_available = DateTimeField(model_attr='date_available')
    date_update = DateTimeField(model_attr='date_update')

    def get_updated_field(self):
        return 'date_update'

    def get_model(self):
        return Document

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(
            date_available__lte=timezone.now(),
            published=True)
