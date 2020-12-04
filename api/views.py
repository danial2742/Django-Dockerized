from rest_framework import filters
from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from rest_framework_tracking.mixins import LoggingMixin
from api.serializers import UserSerializer, GroupSerializer
from django_filters.rest_framework import DjangoFilterBackend


class UserViewSet(LoggingMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = []
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]

    ordering_fields = ['username', 'email']
    search_fields = ['username', 'email']
    filterset_fields = ['username', 'email']


class GroupViewSet(LoggingMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = []