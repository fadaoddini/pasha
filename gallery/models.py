from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.contrib.auth import get_user_model as user_model
from django.db import models, transaction


class Gallery(models.Model):

    ACTIVE = True
    INACTIVE = False

    User = user_model()
    user = models.ForeignKey(User, related_name='galleries', on_delete=models.RESTRICT)
    description = RichTextUploadingField(blank=True)
    is_active = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'گالری'
        verbose_name_plural = "گالری"

    def __str__(self):
        return self.description

    @classmethod
    def add_gallery(cls, request, *args, **kwargs):
        result = "200"
        is_active =True
        form = request.POST
        user = request.user
        description = form.get('description')
        numpic = form.get('numpic')
        numpic = int(numpic)+1

        with transaction.atomic():
            new_gallery = Gallery(user=user, description=description, is_active=is_active)
            new_gallery.save()
            new_product_pk = new_gallery.pk
            if numpic >= 0:

                for i in range(numpic):
                    if request.FILES.get(f'image{i}') is None:
                        pass
                    else:
                        ali =request.FILES.get(f'image{i}')
                        new_image = GalleryImage.add_images(request.FILES[f'image{i}'], new_gallery)

            result = "100"
        return result


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='galleries/', null=True, blank=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return str(self.gallery)

    @classmethod
    def add_images(cls, image, gallery):
        new_image = GalleryImage(image=image, gallery=gallery)
        new_image.save()
        return new_image
