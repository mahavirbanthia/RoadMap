# Generated by Django 3.0.8 on 2020-10-05 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rm', '0005_auto_20201005_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
