from django.contrib import messages
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from gallery import forms
from gallery.forms import GalleryForm, GalleryImageFormSet
from gallery.models import Gallery


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


class GalleryListWeb(View):
    template_name = 'web/admin/gallery/index.html'

    def get(self, request, *args, **kwargs):
        context = dict()
        gallerys = Gallery.objects.all()
        print("gallerys")
        print(gallerys)
        print("gallerys")
        count_gallerys = gallerys.count()
        context['gallerys'] = gallerys
        context['count_gallerys'] = count_gallerys
        return render(request, template_name=self.template_name, context=context,
                      content_type=None, status=None, using=None)


class AddGallery(View):
    template_name_learn = 'web/admin/gallery/index.html'
    template_name = 'web/admin/gallery/add.html'

    def get(self, request, *args, **kwargs):
        context = dict()
        form_gallery = GalleryForm()
        context['form_gallery'] = form_gallery
        return render(request, template_name=self.template_name, context=context,
                      content_type=None, status=None, using=None)

    def post(self, request, *args, **kwargs):
        context = dict()
        gallerys = Gallery.objects.all()
        context['gallerys'] = gallerys
        result = Gallery.add_gallery(request)
        if result == "100":
            return HttpResponseRedirect(reverse_lazy('gallery-list-admin'))
        return HttpResponseRedirect(reverse_lazy('gallery-list-admin'))


class EditGallery(View):
    template_name_learn = 'web/admin/gallery/index.html'
    template_name = 'web/admin/gallery/edit.html'

    def get(self, request, pk, *args, **kwargs):
        context = dict()
        gallery = Gallery.objects.filter(pk=pk).first()
        form_gallery = GalleryForm(instance=gallery)
        form_gallery_images = GalleryImageFormSet(instance=gallery)

        context['form_gallery_images'] = form_gallery_images
        context['form_gallery'] = form_gallery
        context['gallery'] = gallery
        return render(request, template_name=self.template_name, context=context,
                      content_type=None, status=None, using=None)

    def post(self, request, pk, *args):
        context = dict()
        gallerys = Gallery.objects.all()
        context['gallerys'] = gallerys
        gallery = Gallery.objects.filter(pk=pk).first()
        context['gallery'] = gallery
        if gallery:
            form = forms.GalleryForm(request.POST, request.FILES, instance=gallery)
        else:
            form = forms.GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            Gallery.add_gallery(request)
            messages.info(request, " با موفقیت ثبت شد")
            return HttpResponseRedirect(reverse_lazy('gallery-list-admin'))
        else:
            messages.error(request, "با خطا روبرو شد!")

        return HttpResponseRedirect(reverse_lazy('gallery-list-admin'))
