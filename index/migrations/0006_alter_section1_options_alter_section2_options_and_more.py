# Generated by Django 4.2 on 2024-06-01 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_remove_section4_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='section1',
            options={'verbose_name': 'بخش اول', 'verbose_name_plural': 'بخش اول'},
        ),
        migrations.AlterModelOptions(
            name='section2',
            options={'verbose_name': 'بخش دوم', 'verbose_name_plural': 'بخش دوم'},
        ),
        migrations.AlterModelOptions(
            name='section3',
            options={'verbose_name': 'بخش سوم', 'verbose_name_plural': 'بخش سوم'},
        ),
        migrations.AlterModelOptions(
            name='section4',
            options={'verbose_name': 'بخش چهارم', 'verbose_name_plural': 'بخش چهارم'},
        ),
        migrations.AlterModelOptions(
            name='section5',
            options={'verbose_name': 'بخش پنجم', 'verbose_name_plural': 'بخش پنجم'},
        ),
        migrations.AlterModelOptions(
            name='section6',
            options={'verbose_name': 'بخش ششم', 'verbose_name_plural': 'بخش ششم'},
        ),
        migrations.AlterModelOptions(
            name='settingapp',
            options={'verbose_name': 'تنظیمات', 'verbose_name_plural': 'تنظیمات'},
        ),
    ]
