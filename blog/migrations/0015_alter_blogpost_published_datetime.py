# Generated by Django 4.2.7 on 2023-12-14 21:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_blogpost_published_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='published_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
