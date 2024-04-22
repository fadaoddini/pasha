from django.shortcuts import render
from django.views import View


class AboutIndex(View):
    template_name = 'web/about/index.html'

