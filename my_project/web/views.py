from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
def ok_to_load_in_a_frame(request):
    return HttpResponse("his page is safe to load in a frame on any site.")


class LandingPageView(TemplateView):
    template_name = 'landing_page.html'
