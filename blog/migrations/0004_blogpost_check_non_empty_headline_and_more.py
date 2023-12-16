# Generated by Django 4.2.7 on 2023-11-18 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogpost_author'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='blogpost',
            constraint=models.CheckConstraint(check=models.Q(('headline', '')), name='check_non_empty_headline', violation_error_message='Headline cannot be empty'),
        ),
        migrations.AddConstraint(
            model_name='blogpost',
            constraint=models.CheckConstraint(check=models.Q(('author', '')), name='check_non_empty_author', violation_error_message='Author cannot be empty'),
        ),
    ]