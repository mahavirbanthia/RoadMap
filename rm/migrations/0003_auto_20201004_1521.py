# Generated by Django 3.0.8 on 2020-10-04 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rm', '0002_auto_20201004_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='brief_desc',
            field=models.CharField(default='', max_length=15000),
        ),
        migrations.AlterField(
            model_name='course',
            name='short_desc',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
