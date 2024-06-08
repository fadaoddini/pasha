from django.urls import path, re_path

from blog.views import blog_list, category_blog_list, detail_blog, SingleBlogWeb, BlogWeb, BlogWebPk, AddBlog, \
    BlogListWeb, EditBlog, BlogList
from contact.views import MainContact, AddContact

urlpatterns = [
    path('', MainContact.as_view(), name='contact'),
    path('add_contact/', AddContact.as_view(), name='add-contact'),
]
