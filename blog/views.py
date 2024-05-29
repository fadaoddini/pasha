from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from blog import forms
from blog.forms import BlogForm
from blog.models import Blog, Category
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


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
    template_name = 'web/blog/index.html'

    def get(self, request, *args, **kwargs):
        context = dict()
        categories = Category.objects.prefetch_related('blogs').all()
        blogs = Blog.objects.select_related('category').filter(status=True).all()
        print(categories[0].blogs.all())
        context['blogs'] = blogs
        context['categories'] = categories
        return render(request, template_name=self.template_name, context=context,
                      content_type=None, status=None, using=None)


class BlogListWeb(View):
    template_name = 'web/admin/blog/index.html'

    def get(self, request, *args, **kwargs):
        context = dict()
        categories = Category.objects.prefetch_related('blogs').all()
        blogs = Blog.objects.select_related('category').all()
        context['blogs'] = blogs
        context['categories'] = categories
        return render(request, template_name=self.template_name, context=context,
                      content_type=None, status=None, using=None)


class BlogWebPk(View):
    template_name = 'web/blog/blog.html'

    def get(self, request, pk, *args, **kwargs):
        context = dict()
        category = Category.objects.filter(pk=pk).first()
        blogs = Blog.objects.filter(category=pk).all()
        context['blogs'] = blogs
        context['category'] = category
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
            blog.save()
            messages.info(request, "وبلاگ با موفقیت ثبت شد")
            return HttpResponseRedirect(reverse_lazy('blog-web'))
        else:
            messages.error(request, "با خطا روبرو شد!")

        return HttpResponseRedirect(reverse_lazy('blog-web'))

