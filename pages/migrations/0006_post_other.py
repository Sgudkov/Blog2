# Generated by Django 2.2.7 on 2019-12-09 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20191209_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='other',
            field=models.BooleanField(default=False),
        ),
    ]
