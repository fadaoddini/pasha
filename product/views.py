from django.shortcuts import render
from django.views import View

from config.utils import CustomPagination
from product.models import Category, Product


class ProductIndex(View):
    template_name = 'web/product/index.html'

    def get(self, request, *args, **kwargs):
        context = dict()
        categories = Category.objects.prefetch_related('blogs').all()
        products = Product.objects.select_related('category').all()
        count_products = products.count()
        context['products'] = products
        new_context = CustomPagination.create_paginator(products, 7, 3, context, request)
        context['paginator'] = new_context['paginator']
        context['page_obj'] = new_context['page_obj']
        context['limit_number'] = new_context['limit_number']
        context['num_pages'] = new_context['num_pages']
        context['categories'] = categories
        context['count_blogs'] = count_products

        return render(request, template_name=self.template_name, context=context,
                      content_type=None, status=None, using=None)


class ProductWebPk(View):
    template_name = 'web/product/single.html'

    def get(self, request, pk, *args, **kwargs):
        context = dict()
        product = Product.objects.filter(pk=pk).first()
        category_id = product.category.pk
        products = Product.objects.filter(category=category_id).all()
        context['product'] = product
        context['products'] = products
        return render(request, template_name=self.template_name, context=context,
                      content_type=None, status=None, using=None)
