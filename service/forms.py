from django import forms

from service.models import Service


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'lid', 'description', 'image', 'category', 'status']

        widgets = {'description': forms.Textarea()}


