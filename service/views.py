from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from service import forms
from service.forms import ServiceForm
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


class ServiceListWeb(View):
    template_name = 'web/admin/service/index.html'

    def get(self, request, *args, **kwargs):
        context = dict()
        categories = Category.objects.prefetch_related('services').all()
        services = Service.objects.select_related('category').all()
        print("services")
        print(services)
        print("services")
        count_services = services.count()
        context['services'] = services
        context['count_services'] = count_services
        context['categories'] = categories
        return render(request, template_name=self.template_name, context=context,
                      content_type=None, status=None, using=None)


class AddService(View):
    template_name_learn = 'web/admin/service/index.html'
    template_name = 'web/admin/service/add.html'

    def get(self, request, *args, **kwargs):
        context = dict()
        form_service = ServiceForm()
        context['form_service'] = form_service
        return render(request, template_name=self.template_name, context=context,
                      content_type=None, status=None, using=None)

    def post(self, request, *args, **kwargs):
        context = dict()
        services = Service.objects.all()
        context['services'] = services

        form = forms.ServiceForm(request.POST, request.FILES)

        if form.is_valid():
            service = form.save(commit=False)
            service.user = request.user
            service.hit = 1
            service.save()
            messages.info(request, "خدمات با موفقیت ثبت شد")
            return HttpResponseRedirect(reverse_lazy('service-list-admin'))
        else:
            messages.error(request, "با خطا روبرو شد!")

        return HttpResponseRedirect(reverse_lazy('service-list-admin'))


class EditService(View):
    template_name_learn = 'web/admin/service/index.html'
    template_name = 'web/admin/service/edit.html'

    def get(self, request, pk, *args, **kwargs):
        context = dict()
        service = Service.objects.filter(pk=pk).first()
        form_service = ServiceForm(instance=service)
        context['form_service'] = form_service
        context['service'] = service
        return render(request, template_name=self.template_name, context=context,
                      content_type=None, status=None, using=None)

    def post(self, request, pk, *args, **kwargs):
        context = dict()
        blogs = Service.objects.all()
        context['blogs'] = blogs
        service = Service.objects.filter(pk=pk).first()
        context['service'] = service
        if service:
            form = forms.ServiceForm(request.POST, request.FILES, instance=service)
        else:
            form = forms.ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            serviceform = form.save(commit=False)
            serviceform.user = request.user
            serviceform.save()
            messages.info(request, "خدمات با موفقیت ثبت شد")
            return HttpResponseRedirect(reverse_lazy('service-list-admin'))
        else:
            messages.error(request, "با خطا روبرو شد!")

        return HttpResponseRedirect(reverse_lazy('service-list-admin'))




