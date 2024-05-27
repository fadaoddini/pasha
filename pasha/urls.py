
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from pasha.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include('about.urls')),
    path('', include('index.urls')),
    path('service/', include('service.urls')),
    path('admin_web/', include('adminweb.urls')),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
