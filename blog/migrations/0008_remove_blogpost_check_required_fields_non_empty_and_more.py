# Generated by Django 4.2.7 on 2023-11-18 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_blogpost_check_required_fields_non_empty_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='blogpost',
            name='check_required_fields_non_empty',
        ),
        migrations.AddConstraint(
            model_name='blogpost',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('headline', ''), _negated=True), models.Q(('author', ''), _negated=True)), name='check_required_fields_non_empty', violation_error_message='Required fields (headline, author) cannot be empty'),
        ),
    ]
