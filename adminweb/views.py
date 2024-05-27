from django.shortcuts import render
from django.views import View


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
