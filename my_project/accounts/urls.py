from django.urls import path
from accounts import views


urlpatterns = [
    path('login', views.LoginAccView.as_view(), name='login'),

]
