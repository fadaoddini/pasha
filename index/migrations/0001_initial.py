# Generated by Django 4.2 on 2024-04-23 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SettingApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True)),
                ('favicon', models.ImageField(blank=True, null=True, upload_to='settings/')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='settings/')),
                ('login_text', models.TextField(blank=True)),
                ('tel', models.CharField(blank=True, max_length=15, null=True)),
                ('mobile', models.CharField(blank=True, max_length=11, null=True)),
                ('address', models.TextField(blank=True)),
                ('email', models.CharField(blank=True, max_length=30, null=True)),
                ('about_text', models.TextField(blank=True)),
                ('footer_text', models.TextField(blank=True)),
                ('is_active', models.BooleanField(choices=[(True, 'active'), (False, 'inactive')], default=True)),
            ],
            options={
                'verbose_name': 'setting',
                'verbose_name_plural': 'settings',
            },
        ),
    ]
