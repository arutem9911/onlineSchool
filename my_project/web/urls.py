from django.urls import path
from web.views import LandingPageView


urlpatterns = [
   path('', LandingPageView.as_view(), name='main')
]
