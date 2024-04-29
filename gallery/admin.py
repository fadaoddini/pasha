from django.contrib import admin
from django.contrib.admin import register

from gallery.models import GalleryImage, Gallery


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 2


@register(Gallery)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('is_active',)
    search_fields = ('user',)
    actions = ('active_all', 'deactive_all')
    inlines = [GalleryImageInline, ]

    def active_all(self, request, queryset):
        for queryone in queryset:
            gallery = Gallery.objects.filter(pk=queryone.pk).first()
            gallery.is_active = True
            gallery.save()

    def deactive_all(self, request, queryset):
            for queryone in queryset:
                gallery = Gallery.objects.filter(pk=queryone.pk).first()
                gallery.is_active = False
                gallery.save()


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('images',)
