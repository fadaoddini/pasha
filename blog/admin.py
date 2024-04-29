from django.contrib import admin

from blog.models import Blog, Category
from django.contrib.admin import register

from index.models import Section1, Section6, Section5, Section4, Section3, Section2


# Register your models here.


@register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'status')
    list_filter = ('user', 'status', 'category')
    list_editable = ('status',)
    search_fields = ('category', 'user')
    actions = ('active_all', 'deactive_all')

    def active_all(self, request, queryset):
        for queryone in queryset:
            blog = Blog.objects.filter(pk=queryone.pk).first()
            blog.status = True
            blog.save()

    def deactive_all(self, request, queryset):
            for queryone in queryset:
                blog = Blog.objects.filter(pk=queryone.pk).first()
                blog.status = False
                blog.save()


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name',)


@register(Section1)
class Section1Admin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title',)


@register(Section2)
class Section2Admin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title',)


@register(Section3)
class Section3Admin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title',)


@register(Section4)
class Section4Admin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title',)


@register(Section5)
class Section5Admin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title',)


@register(Section6)
class Section6Admin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title',)

