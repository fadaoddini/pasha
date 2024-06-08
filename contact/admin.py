from django.contrib import admin
from django.contrib.admin import register

from contact.models import Contact


@register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'family', 'mobile', 'email', 'status')
    list_filter = ('status', )
    list_editable = ('status',)
    search_fields = ('mobile', 'email', 'family')
    actions = ('active_all', 'deactive_all')

    def active_all(self, request, queryset):
        for queryone in queryset:
            contact = Contact.objects.filter(pk=queryone.pk).first()
            contact.status = True
            contact.save()

    def deactive_all(self, request, queryset):
            for queryone in queryset:
                contact = Contact.objects.filter(pk=queryone.pk).first()
                contact.status = False
                contact.save()

