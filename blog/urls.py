from django.urls import path, re_path

from blog.views import blog_list, category_blog_list, detail_blog, SingleBlogWeb, BlogWeb, BlogWebPk, AddBlog, \
    BlogListWeb, EditBlog, BlogList

urlpatterns = [
    path('blog/admin/list/', BlogListWeb.as_view(), name='blog-list-admin'),
    path('detail/<str:title>', detail_blog),
    path('categories/list/', category_blog_list),
    path('archive/<int:year>/', blog_list),
    re_path(r'archive/?P<year>[0-9]{4}/', blog_list),
    path('single/<int:pk>/', SingleBlogWeb.as_view(), name='blog-single-web'),
    path('blog/', BlogWeb.as_view(), name='blog-web'),
    path('blog/<int:pk>/', BlogWebPk.as_view(), name='blog-web-pk'),
    path('archive/<int:year>/<int:month>/', blog_list),
    path('add_blog/', AddBlog.as_view(), name='add-blog'),
    path('edit_blog/<int:pk>/', EditBlog.as_view(), name='edit-blog'),
    path('', BlogList.as_view(), name='blog-list'),
]
