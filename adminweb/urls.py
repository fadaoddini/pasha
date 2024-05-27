from django.urls import path, re_path

from adminweb.views import AdminWebIndex

urlpatterns = [
    path('', AdminWebIndex.as_view(), name='admin_web-index'),
]