# Generated by Django 2.2.7 on 2019-12-09 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_post_fm'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='decs',
            field=models.CharField(default='Description', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='head',
            field=models.CharField(max_length=50),
        ),
    ]