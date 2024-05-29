from django.urls import path, re_path

from gallery.views import AddGallery, EditGallery, GalleryListWeb

urlpatterns = [

    path('add_service/', AddGallery.as_view(), name='add-gallery'),
    path('edit_service/<int:pk>/', EditGallery.as_view(), name='edit-gallery'),
    path('service/admin/list/', GalleryListWeb.as_view(), name='gallery-list-admin'),
]
