from rest_framework import viewsets
from rest_framework.exceptions import NotFound
import django_filters

from categories.serializers import CategorySerializer
from projects.serializers import ProjectSerializer
from projects.models import Project


class ProjectFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(name='categories__name',
                                         lookup_type='iexact')

    class Meta:
        model = Project


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'slug'
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_class = ProjectFilter
    filter_fields = Project._meta.get_all_field_names()
