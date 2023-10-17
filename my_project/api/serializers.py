from rest_framework import serializers
from accounts.models import User, StudyGroup, UserGroup
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'first_name',
                  'last_name', 'username',
                  'email', 'phone',
                  'photo', 'role',
                  'birth_date',
                  'city']
        read_only = ['id', 'username']


class StudyGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyGroup
        fields = ['id', 'title', 'start_date', 'end_date', 'lesson']
        read_only = ['id']


class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = ['id', 'user', 'group']
        read_only = ['id']
