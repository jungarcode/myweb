# Generated by Django 5.1.2 on 2024-11-09 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0003_alter_post_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="published",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
