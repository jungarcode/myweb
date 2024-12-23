# Generated by Django 5.1.2 on 2024-10-29 14:08

from django_ckeditor_5.fields import CKEditor5Field

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('state', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True)),
                ('slug', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(max_length=110)),
                ('content', CKEditor5Field()),
                ('published', models.DateTimeField(default=datetime.datetime(2024, 10, 29, 14, 8, 53, 697453, tzinfo=datetime.timezone.utc))),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('state', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('categories', models.ManyToManyField(to='web.category')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['-created'],
            },
        ),
    ]
