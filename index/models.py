from django.db import models

from service.models import Category


class SettingApp(models.Model):
    ACTIVE = True
    INACTIVE = False

    STATUS_OPEN = (
        (ACTIVE, 'active'),
        (INACTIVE, 'inactive'),
    )
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    favicon = models.ImageField(upload_to='settings/', null=True, blank=True)
    logo = models.ImageField(upload_to='settings/', null=True, blank=True)
    login_text = models.TextField(blank=True)
    tel = models.CharField(max_length=15, blank=True, null=True)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    address = models.TextField(blank=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    about_text = models.TextField(blank=True)
    footer_text = models.TextField(blank=True)
    is_active = models.BooleanField(choices=STATUS_OPEN, default=ACTIVE)

    class Meta:
        verbose_name = 'setting'
        verbose_name_plural = 'settings'

    def __str__(self):
        return self.title


class Section1(models.Model):
    title = models.CharField(max_length=120)
    lid = models.TextField(blank=True)
    description = models.TextField(blank=True)
    image1 = models.ImageField(upload_to='%Y/index/%m/%d/', null=True, blank=True)
    image2 = models.ImageField(upload_to='%Y/index/%m/%d/', null=True, blank=True)
    film = models.FileField(upload_to='%Y/index/%m/%d/', null=True, blank=True)
    img1 = models.ImageField(upload_to='%Y/index/%m/%d/', null=True, blank=True)
    img2 = models.ImageField(upload_to='%Y/index/%m/%d/', null=True, blank=True)
    img3 = models.ImageField(upload_to='%Y/index/%m/%d/', null=True, blank=True)
    text1 = models.CharField(max_length=120)
    text2 = models.CharField(max_length=120)
    text3 = models.CharField(max_length=120)

    class Meta:
        verbose_name = 'section1'
        verbose_name_plural = 'sections1'

    def __str__(self):
        return "بخش اول"


class Section2(models.Model):
    title = models.CharField(max_length=120)
    lid = models.TextField(blank=True)
    description = models.TextField(blank=True)
    image1 = models.ImageField(upload_to='%Y/index/%m/%d/', null=True, blank=True)
    image2 = models.ImageField(upload_to='%Y/index/%m/%d/', null=True, blank=True)
    image3 = models.ImageField(upload_to='%Y/index/%m/%d/', null=True, blank=True)
    image4 = models.ImageField(upload_to='%Y/index/%m/%d/', null=True, blank=True)
    icon1 = models.ImageField(upload_to='%Y/index/%m/%d/', null=True, blank=True)
    icon2 = models.ImageField(upload_to='%Y/index/%m/%d/', null=True, blank=True)
    text1 = models.CharField(max_length=120)
    text2 = models.CharField(max_length=120)

    class Meta:
        verbose_name = 'section2'
        verbose_name_plural = 'sections2'

    def __str__(self):
        return "بخش دوم"


class Section3(models.Model):
    title = models.CharField(max_length=120)
    lid = models.TextField(blank=True)
    footer = models.TextField(blank=True)

    class Meta:
        verbose_name = 'section3'
        verbose_name_plural = 'sections3'

    def __str__(self):
        return "بخش سوم"


class Section4(models.Model):
    title = models.CharField(max_length=120)
    lid = models.TextField(blank=True)
    image = models.ImageField(upload_to='%Y/index/%m/%d/', null=True, blank=True)
    film = models.FileField(upload_to='%Y/index/%m/%d/', null=True, blank=True)
    text_ok = models.CharField(max_length=120)
    icon_ok = models.ImageField(upload_to='%Y/index/%m/%d/', null=True, blank=True)
    num_ok = models.PositiveBigIntegerField()
    text_project = models.CharField(max_length=120)
    icon_project = models.ImageField(upload_to='%Y/index/%m/%d/', null=True, blank=True)
    num_project = models.PositiveBigIntegerField()
    text_tajrobe = models.CharField(max_length=120)
    icon_tajrobe = models.ImageField(upload_to='%Y/index/%m/%d/', null=True, blank=True)
    num_tajrobe = models.PositiveBigIntegerField()
    text_person = models.CharField(max_length=120)
    icon_person = models.ImageField(upload_to='%Y/index/%m/%d/', null=True, blank=True)
    num_person = models.PositiveBigIntegerField()

    class Meta:
        verbose_name = 'section4'
        verbose_name_plural = 'sections4'

    def __str__(self):
        return "بخش چهارم"


class Section5(models.Model):
    title = models.CharField(max_length=120)
    lid = models.TextField(blank=True)
    footer = models.TextField(blank=True)

    class Meta:
        verbose_name = 'section5'
        verbose_name_plural = 'sections5'

    def __str__(self):
        return "بخش پنجم"


class Section6(models.Model):
    title = models.CharField(max_length=120)
    lid = models.TextField(blank=True)
    footer = models.TextField(blank=True)

    class Meta:
        verbose_name = 'section6'
        verbose_name_plural = 'sections6'

    def __str__(self):
        return "بخش ششم"