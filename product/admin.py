from django.contrib import admin
from django.contrib.admin import register

from product.models import Product, Category


@register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'weight', 'status')
    list_filter = ('user', 'status', 'category', 'weight')
    list_editable = ('status',)
    search_fields = ('category', 'user', 'weight')
    actions = ('active_all', 'deactive_all')

    def active_all(self, request, queryset):
        for queryone in queryset:
            product = Product.objects.filter(pk=queryone.pk).first()
            product.status = True
            product.save()

    def deactive_all(self, request, queryset):
            for queryone in queryset:
                product = Product.objects.filter(pk=queryone.pk).first()
                product.status = False
                product.save()


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name',)


