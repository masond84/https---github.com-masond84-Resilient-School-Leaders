# Generated by Django 4.2 on 2023-06-11 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0006_category_template_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='template_name',
        ),
    ]
