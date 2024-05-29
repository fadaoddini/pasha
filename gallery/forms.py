from django import forms
from django.forms import inlineformset_factory

from gallery.models import Gallery, GalleryImage


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['description', 'is_active']

        widgets = {'description': forms.Textarea()}


class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        exclude = ()


GalleryImageFormSet = inlineformset_factory(Gallery, GalleryImage, form=GalleryImageForm, extra=2)


