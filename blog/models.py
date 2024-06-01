from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.contrib.auth import get_user_model as user_model
from tinymce.models import HTMLField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=32)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)

    class Meta:
        verbose_name = 'دسته بندی وبلاگ'
        verbose_name_plural = "دسته بندی بلاگ"

    def __str__(self):
        return self.name


class Blog(models.Model):
    ACTIVE = True
    INACTIVE = False

    STATUS_INFO = (
        (ACTIVE, 'active'),
        (INACTIVE, 'inactive'),
    )

    User = user_model()
    title = models.CharField(max_length=50)
    lid = models.CharField(max_length=50)
    hit = models.PositiveBigIntegerField(blank=True)
    description = RichTextUploadingField(blank=True)
    image = models.ImageField(upload_to='%Y/%m/%d/blogs/', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blogs')
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    status = models.BooleanField(choices=STATUS_INFO, default=INACTIVE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"({self.title}):{self.user}"

    class Meta:
        verbose_name = 'وبلاگ'
        verbose_name_plural = "بلاگ ها"