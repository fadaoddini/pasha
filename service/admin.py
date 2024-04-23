from django.contrib import admin

from service.models import Service, Category
from django.contrib.admin import register

# Register your models here.


@register(Service)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'status', 'show_web')
    list_filter = ('user', 'status', 'category')
    list_editable = ('status', 'show_web')
    search_fields = ('category', 'user')
    actions = ('active_all', 'deactive_all')

    def active_all(self, request, queryset):
        for queryone in queryset:
            blog = Service.objects.filter(pk=queryone.pk).first()
            blog.status = True
            blog.save()

    def deactive_all(self, request, queryset):
            for queryone in queryset:
                blog = Service.objects.filter(pk=queryone.pk).first()
                blog.status = False
                blog.save()


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name',)

