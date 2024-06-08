from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from blog import forms
from blog.forms import BlogForm
from blog.models import Blog, Category
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from config.utils import CustomPagination


def blog_list(request, year=None, month=None):
    if month is not None:
        return HttpResponse(f"blog list {year} - {month}")
    if year is not None:
        return HttpResponse(f"blog list {year}")

    return HttpResponse(f"blog list")


def category_blog_list(request):
    return HttpResponse("category_blog_list")


def detail_blog(request, title):
    return HttpResponse(f"detail_blog {title}")


class SingleBlogWeb(View):
    template_name = 'web/blog/single.html'

    def get(self, request, pk, *args, **kwargs):
        context = dict()
        blog = Blog.objects.filter(pk=pk).first()
        context['blog'] = blog
        return render(request, template_name=self.template_name, context=context,
                      content_type=None, status=None, using=None)


class BlogWeb(View):
    template_name = 'web/admin/blog/index.html'

    def get(self, request, *args, **kwargs):
        context = dict()
        categories = Category.objects.prefetch_related('blogs').all()
        blogs = Blog.objects.select_related('category').all()
        count_blogs = blogs.count()
        context['blogs'] = blogs
        context['categories'] = categories
        context['count_blogs'] = count_blogs
        return render(request, template_name=self.template_name, context=context,
                      content_type=None, status=None, using=None)


class BlogListWeb(View):
    template_name = 'web/admin/blog/index.html'

    def get(self, request, *args, **kwargs):
        context = dict()
        categories = Category.objects.prefetch_related('blogs').all()
        blogs = Blog.objects.select_related('category').all()
        count_blogs = blogs.count()
        context['blogs'] = blogs
        context['count_blogs'] = count_blogs
        context['categories'] = categories
        return render(request, template_name=self.template_name, context=context,
                      content_type=None, status=None, using=None)


class AddBlog(View):
    template_name_learn = 'web/admin/blog/index.html'
    template_name = 'web/admin/blog/add.html'

    def get(self, request, *args, **kwargs):
        context = dict()
        form_blog = BlogForm()
        context['form_blog'] = form_blog
        return render(request, template_name=self.template_name, context=context,
                      content_type=None, status=None, using=None)

    def post(self, request, *args, **kwargs):
        context = dict()
        blogs = Blog.objects.all()
        context['blogs'] = blogs

        form = forms.BlogForm(request.POST, request.FILES)

        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.hit = 1
            blog.save()
            messages.info(request, "وبلاگ با موفقیت ثبت شد")
            return HttpResponseRedirect(reverse_lazy('blog-web'))
        else:
            messages.error(request, "با خطا روبرو شد!")

        return HttpResponseRedirect(reverse_lazy('blog-web'))


class EditBlog(View):
    template_name_learn = 'web/admin/blog/index.html'
    template_name = 'web/admin/blog/edit.html'

    def get(self, request, pk, *args, **kwargs):
        context = dict()
        blog = Blog.objects.filter(pk=pk).first()
        form_blog = BlogForm(instance=blog)
        context['form_blog'] = form_blog
        context['blog'] = blog
        return render(request, template_name=self.template_name, context=context,
                      content_type=None, status=None, using=None)

    def post(self, request, pk, *args, **kwargs):
        context = dict()
        blogs = Blog.objects.all()
        context['blogs'] = blogs
        blog = Blog.objects.filter(pk=pk).first()
        context['blog'] = blog
        if blog:
            form = forms.BlogForm(request.POST, request.FILES, instance=blog)
        else:
            form = forms.BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blogform = form.save(commit=False)
            blogform.user = request.user
            blogform.save()
            messages.info(request, "وبلاگ با موفقیت ثبت شد")
            return HttpResponseRedirect(reverse_lazy('blog-web'))
        else:
            messages.error(request, "با خطا روبرو شد!")

        return HttpResponseRedirect(reverse_lazy('blog-web'))


class BlogList(View):
    template_name = 'web/blog/index.html'

    def get(self, request, *args, **kwargs):
        context = dict()
        categories = Category.objects.prefetch_related('blogs').all()
        blogs = Blog.objects.select_related('category').all()
        count_blogs = blogs.count()
        context['blogs'] = blogs
        new_context = CustomPagination.create_paginator(blogs, 8, 3, context, request)
        context['paginator'] = new_context['paginator']
        context['page_obj'] = new_context['page_obj']
        context['limit_number'] = new_context['limit_number']
        context['num_pages'] = new_context['num_pages']
        context['categories'] = categories
        context['count_blogs'] = count_blogs
        return render(request, template_name=self.template_name, context=context,
                      content_type=None, status=None, using=None)


class BlogWebPk(View):
    template_name = 'web/blog/single.html'

    def get(self, request, pk, *args, **kwargs):
        context = dict()
        blog = Blog.objects.filter(pk=pk).first()
        context['blog'] = blog
        return render(request, template_name=self.template_name, context=context,
                      content_type=None, status=None, using=None)
