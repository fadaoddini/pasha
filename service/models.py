from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.contrib.auth import get_user_model as user_model
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=32)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)
    icon_w = models.ImageField(upload_to='%Y/service/category/%m/%d', null=True, blank=True)
    icon_b = models.ImageField(upload_to='%Y/service/category/%m/%d', null=True, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Service(models.Model):
    ACTIVE = True
    INACTIVE = False

    STATUS_INFO = (
        (ACTIVE, 'active'),
        (INACTIVE, 'inactive'),
    )

    User = user_model()
    title = models.CharField(max_length=50)
    lid = models.CharField(max_length=50)
    hit = models.PositiveBigIntegerField()
    description = RichTextUploadingField(blank=True)
    image = models.ImageField(upload_to='%Y/service/service/%m/%d', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userblogs')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='services')
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    status = models.BooleanField(choices=STATUS_INFO, default=INACTIVE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    show_web = models.BooleanField(choices=STATUS_INFO, default=INACTIVE)

    def __str__(self):
        return f"({self.title}):{self.user}"