from django.urls import path, re_path

from about.views import AboutIndex

urlpatterns = [
    path('index/', AboutIndex.as_view()),
]