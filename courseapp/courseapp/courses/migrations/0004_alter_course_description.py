# Generated by Django 4.1.7 on 2023-03-06 10:16

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]