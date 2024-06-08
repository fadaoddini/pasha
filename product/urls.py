from django.urls import path, re_path

from product.views import ProductIndex, ProductWebPk

urlpatterns = [
    path('', ProductIndex.as_view(), name='products'),
    path('product/<int:pk>/', ProductWebPk.as_view(), name='product-web-pk'),
]