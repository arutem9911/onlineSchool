from django.urls import path, include
from accounts import views
from rest_framework import routers
from .views import UserViewSet, GroupViewSet, UserGroupVewSet
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('group', GroupViewSet)
router.register('userGroup', UserGroupVewSet)


urlpatterns = [
    path('', include(router.urls))
]

