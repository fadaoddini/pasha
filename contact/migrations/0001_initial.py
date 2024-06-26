# Generated by Django 4.2 on 2024-06-07 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('family', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=11)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('lid', models.TextField(blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(choices=[(True, 'active'), (False, 'inactive')], default=False)),
            ],
            options={
                'verbose_name': 'تماس با ما',
                'verbose_name_plural': 'تماس با ما',
            },
        ),
    ]
