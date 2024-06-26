from django.urls import path, re_path

from service.views import service_list, category_blog_list, detail_blog, SingleServiceWeb, ServiceWeb, ServiceWebPk, \
    AddService, ServiceListWeb, EditService

urlpatterns = [
    path('list/', service_list),
    path('detail/<str:title>', detail_blog),
    path('categories/list/', category_blog_list),
    path('archive/<int:year>/', service_list),
    re_path(r'archive/?P<year>[0-9]{4}/', service_list),
    path('single/<int:pk>/', SingleServiceWeb.as_view(), name='service-single-web'),
    path('service/', ServiceWeb.as_view(), name='service-web'),
    path('service/<int:pk>/', ServiceWebPk.as_view(), name='service-web-pk'),
    path('archive/<int:year>/<int:month>/', service_list),
    path('add_service/', AddService.as_view(), name='add-service'),
    path('edit_service/<int:pk>/', EditService.as_view(), name='edit-service'),
    path('service/admin/list/', ServiceListWeb.as_view(), name='service-list-admin'),
]
