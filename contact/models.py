from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.contrib.auth import get_user_model as user_model


class Contact(models.Model):
    ACTIVE = True
    INACTIVE = False

    STATUS_INFO = (
        (ACTIVE, 'active'),
        (INACTIVE, 'inactive'),
    )

    name = models.CharField(max_length=50, blank=True)
    family = models.CharField(max_length=50)
    mobile = models.CharField(max_length=11)
    email = models.CharField(max_length=50, blank=True)
    lid = models.TextField(blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    status = models.BooleanField(choices=STATUS_INFO, default=INACTIVE)

    def __str__(self):
        return f"({self.name}):{self.family}"

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = "تماس با ما"
