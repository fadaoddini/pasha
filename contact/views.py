from django.shortcuts import render
from django.views import View
from django.contrib import messages
from config.utils import CustomPagination
from contact import forms
from contact.forms import ContactForm
from contact.models import Contact
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


# Create your views here.
class MainContact(View):
    template_name = 'web/contact/index.html'

    def get(self, request, *args, **kwargs):
        context = dict()
        return render(request, template_name=self.template_name, context=context,
                      content_type=None, status=None, using=None)


class AddContact(View):
    def post(self, request, *args, **kwargs):
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.status = False
            contact.save()
            messages.info(request, "درخواست شما با موفقیت ثبت شد")
            return HttpResponseRedirect(reverse_lazy('index'))
        else:
            messages.error(request, "با خطا روبرو شد!")

        return HttpResponseRedirect(reverse_lazy('index'))
