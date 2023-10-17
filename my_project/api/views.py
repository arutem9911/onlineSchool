from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from accounts.models import User, StudyGroup, UserGroup
from .serializers import UserSerializer, StudyGroupSerializer, UserGroupSerializer
from django.contrib.auth import get_user_model


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'


class GroupViewSet(ModelViewSet):
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'


class UserGroupVewSet(ModelViewSet):
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
