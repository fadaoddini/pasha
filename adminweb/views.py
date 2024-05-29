from django.contrib import messages
from django.shortcuts import render
from django.views import View
from adminweb import forms
from adminweb.forms import SettingAppForm, Section1Form, Section2Form, Section4Form, Section3Form, Section5Form, \
    Section6Form
from index.models import SettingApp, Section1, Section2, Section3, Section4, Section5, Section6

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


class AdminWebIndex(View):
    template_name = 'web/admin/index.html'
    template_not_found = 'web/index/404.html'

    def get(self, request, *args, **kwargs):
        context = dict()
        if request.user.is_anonymous:
            context['user'] = "hello dear ...!"
            print("hello dear ...!")
            return render(request, template_name=self.template_not_found, context=context,
                          content_type=None, status=None, using=None)
        else:
            context['user'] = "hello !"
            print("user not found! ")
        return render(request, template_name=self.template_name, context=context,
                      content_type=None, status=None, using=None)


class UpdateAppSetting(View):
    template_name = 'web/admin/setting/index.html'

    def get(self, request, *args, **kwargs):
        context = dict()
        setting_app = SettingApp.objects.first()
        form_setting_app = SettingAppForm()
        context['form_setting_app'] = form_setting_app
        context['setting_app'] = setting_app
        return render(request, template_name=self.template_name, context=context,
                      content_type=None, status=None, using=None)

    def post(self, request, *args, **kwargs):
        setting_app = SettingApp.objects.first()
        if setting_app:
            form = forms.SettingAppForm(request.POST, request.FILES, instance=setting_app)
        else:
            form = forms.SettingAppForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.info(request, " با موفقیت ثبت شد")
        else:
            messages.error(request, "با خطا روبرو شد!")

        return HttpResponseRedirect(reverse_lazy('update-app-setting'))


class UpdateSection1(View):
    template_name = 'web/admin/main/section1.html'

    def get(self, request, *args, **kwargs):
        context = dict()
        section1 = Section1.objects.first()
        form_section1 = Section1Form()
        context['form_section1'] = form_section1
        context['section1'] = section1
        return render(request, template_name=self.template_name, context=context,
                      content_type=None, status=None, using=None)

    def post(self, request, *args, **kwargs):
        section1 = Section1.objects.first()
        if section1:
            form = forms.Section1Form(request.POST, request.FILES, instance=section1)
        else:
            form = forms.Section1Form(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.info(request, " با موفقیت ثبت شد")
        else:
            messages.error(request, "با خطا روبرو شد!")

        return HttpResponseRedirect(reverse_lazy('update-section1'))


class UpdateSection2(View):
    template_name = 'web/admin/main/section2.html'

    def get(self, request, *args, **kwargs):
        context = dict()
        section2 = Section2.objects.first()
        form_section2 = Section2Form()
        context['form_section2'] = form_section2
        context['section2'] = section2
        return render(request, template_name=self.template_name, context=context,
                      content_type=None, status=None, using=None)

    def post(self, request, *args, **kwargs):
        section2 = Section2.objects.first()
        if section2:
            form = forms.Section2Form(request.POST, request.FILES, instance=section2)
        else:
            form = forms.Section2Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, " با موفقیت ثبت شد")
        else:
            messages.error(request, "با خطا روبرو شد!")

        return HttpResponseRedirect(reverse_lazy('update-section2'))


class UpdateSection3(View):
    template_name = 'web/admin/main/section3.html'

    def get(self, request, *args, **kwargs):
        context = dict()
        section3 = Section3.objects.first()
        form_section3 = Section3Form()
        context['form_section3'] = form_section3
        context['section3'] = section3
        return render(request, template_name=self.template_name, context=context,
                      content_type=None, status=None, using=None)

    def post(self, request, *args, **kwargs):
        section3 = Section3.objects.first()
        if section3:
            form = forms.Section3Form(request.POST, request.FILES, instance=section3)
        else:
            form = forms.Section3Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, " با موفقیت ثبت شد")
        else:
            messages.error(request, "با خطا روبرو شد!")

        return HttpResponseRedirect(reverse_lazy('update-section3'))


class UpdateSection4(View):
    template_name = 'web/admin/main/section4.html'

    def get(self, request, *args, **kwargs):
        context = dict()
        section4 = Section4.objects.first()
        form_section4 = Section4Form()
        context['form_section4'] = form_section4
        context['section4'] = section4
        return render(request, template_name=self.template_name, context=context,
                      content_type=None, status=None, using=None)

    def post(self, request, *args, **kwargs):
        section4 = Section4.objects.first()
        if section4:
            form = forms.Section4Form(request.POST, request.FILES, instance=section4)
        else:
            form = forms.Section4Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, " با موفقیت ثبت شد")
        else:
            messages.error(request, "با خطا روبرو شد!")

        return HttpResponseRedirect(reverse_lazy('update-section4'))


class UpdateSection5(View):
    template_name = 'web/admin/main/section5.html'

    def get(self, request, *args, **kwargs):
        context = dict()
        section5 = Section5.objects.first()
        form_section5 = Section5Form()
        context['form_section5'] = form_section5
        context['section5'] = section5
        return render(request, template_name=self.template_name, context=context,
                      content_type=None, status=None, using=None)

    def post(self, request, *args, **kwargs):
        section5 = Section5.objects.first()
        if section5:
            form = forms.Section5Form(request.POST, request.FILES, instance=section5)
        else:
            form = forms.Section5Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, " با موفقیت ثبت شد")
        else:
            messages.error(request, "با خطا روبرو شد!")

        return HttpResponseRedirect(reverse_lazy('update-section5'))


class UpdateSection6(View):
    template_name = 'web/admin/main/section6.html'

    def get(self, request, *args, **kwargs):
        context = dict()
        section6 = Section6.objects.first()
        form_section6 = Section6Form()
        context['form_section6'] = form_section6
        context['section6'] = section6
        return render(request, template_name=self.template_name, context=context,
                      content_type=None, status=None, using=None)

    def post(self, request, *args, **kwargs):
        section6 = Section6.objects.first()
        if section6:
            form = forms.Section6Form(request.POST, request.FILES, instance=section6)
        else:
            form = forms.Section6Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, " با موفقیت ثبت شد")
        else:
            messages.error(request, "با خطا روبرو شد!")

        return HttpResponseRedirect(reverse_lazy('update-section6'))



