# Generated by Django 5.1.2 on 2024-11-08 03:04

from django_ckeditor_5.fields import CKEditor5Field

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0002_alter_post_content_alter_post_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="content",
            field=CKEditor5Field(),
        ),
    ]

