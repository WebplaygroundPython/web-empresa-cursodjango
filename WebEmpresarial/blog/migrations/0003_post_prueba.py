# Generated by Django 3.0 on 2020-09-19 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200917_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='prueba',
            field=models.ManyToManyField(to='blog.Category', verbose_name='Prueba'),
        ),
    ]