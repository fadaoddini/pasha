from django.shortcuts import render
from django.views import View

from gallery.models import Gallery
from index.models import Section1, Section2, Section3, Section4, Section5, Section6
from service.models import Category, Service


class MainIndex(View):
    template_name = 'web/index/index.html'

    def get(self, request, *args, **kwargs):
        context = dict()
        section1 = Section1.objects.first()
        section2 = Section2.objects.first()
        section3 = Section3.objects.first()
        section4 = Section4.objects.first()
        section5 = Section5.objects.first()
        section6 = Section6.objects.first()
        context['section1'] = section1
        context['section2'] = section2
        context['section3'] = section3
        context['section4'] = section4
        context['section5'] = section5
        context['section6'] = section6
        categories = Category.objects.prefetch_related('services').all()
        services = Service.objects.select_related('category').filter(status=True).all()
        galleries1 = Gallery.objects.all()[1:2]
        galleries2 = Gallery.objects.all()[2:3]
        galleries3 = Gallery.objects.all()[3:5]
        galleries5 = Gallery.objects.all()[4:7]
        context['services'] = services
        context['categories'] = categories
        context['galleries1'] = galleries1
        context['galleries2'] = galleries2
        context['galleries3'] = galleries3
        context['galleries5'] = galleries5
        if request.user.is_anonymous:
            context['user'] = "hello dear ...!"

        else:
            context['user'] = "hello !"

        return render(request, template_name=self.template_name, context=context,
                      content_type=None, status=None, using=None)