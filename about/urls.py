from django.urls import path, re_path

from about.views import AboutIndex

urlpatterns = [
    path('/', AboutIndex.as_view()),
]