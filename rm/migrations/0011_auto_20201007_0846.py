# Generated by Django 3.0.8 on 2020-10-07 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rm', '0010_course_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='brief_desc',
            field=models.TextField(),
        ),
    ]
