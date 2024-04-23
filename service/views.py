from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from service.models import Service, Category


def service_list(request, year=None, month=None):
    if month is not None:
        return HttpResponse(f"service list {year} - {month}")
    if year is not None:
        return HttpResponse(f"service list {year}")

    return HttpResponse(f"service list")


def category_blog_list(request):
    return HttpResponse("category_blog_list")


def detail_blog(request, title):
    return HttpResponse(f"detail_blog {title}")


class SingleServiceWeb(View):
    template_name = 'web/service/single.html'

    def get(self, request, pk, *args, **kwargs):
        context = dict()
        blog = Service.objects.filter(pk=pk).first()
        context['service'] = blog
        return render(request, template_name=self.template_name, context=context,
                      content_type=None, status=None, using=None)


class ServiceWeb(View):
    template_name = 'web/service/index.html'

    def get(self, request, *args, **kwargs):
        context = dict()
        categories = Category.objects.prefetch_related('blogs').all()
        blogs = Service.objects.select_related('category').filter(status=True).all()
        print(categories[0].blogs.all())
        context['blogs'] = blogs
        context['categories'] = categories
        return render(request, template_name=self.template_name, context=context,
                      content_type=None, status=None, using=None)


class ServiceWebPk(View):
    template_name = 'web/service/service.html'

    def get(self, request, pk, *args, **kwargs):
        context = dict()
        category = Category.objects.filter(pk=pk).first()
        blogs = Service.objects.filter(category=pk).all()
        context['blogs'] = blogs
        context['category'] = category
        return render(request, template_name=self.template_name, context=context,
                      content_type=None, status=None, using=None)
