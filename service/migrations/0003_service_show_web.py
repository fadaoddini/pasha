# Generated by Django 4.2 on 2024-04-05 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_service_category_image_delete_blog_service_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='show_web',
            field=models.BooleanField(choices=[(True, 'active'), (False, 'inactive')], default=False),
        ),
    ]
