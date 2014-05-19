from django import forms
from django_filters import Filter
from rest_framework import filters



class IdsFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if request.GET.get('ids[]'):
            return queryset.filter(id__in=request.GET.getlist('ids[]'))
        return queryset

class MultipleNumberFilter(Filter):
    def filter(self, qs, value):
        if value is not None:
            value = value.split("_")
            alias = {self.name + '__in': value}
            return qs.filter(**alias)
        return qs

class NullableNumberFilter(Filter):
    def filter(self, qs, value):
        if value == "NotNull":
            alias = {self.name + '__isnull': True}
            return qs.exclude(**alias)
        elif value is not None:
            return qs.filter(**{self.name: value})

        return qs