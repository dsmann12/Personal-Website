from django.db import models
from django.core import validators
from datetime import datetime
from django.utils import timezone
from blog import utils

# Create your models here.
# create Post class here
class BlogPost(models.Model):
    headline = models.CharField(blank=False, validators=[validators.MinLengthValidator(limit_value=1, message="Headline cannot be empty")], max_length=256)
    author = models.CharField(blank=False, validators=[validators.MinLengthValidator(limit_value=1, message="Author cannot be empty")])
    featured_image = models.CharField(null=True)
    published_datetime = models.DateTimeField(blank=False, default=utils.now)
    modified_datetime = models.DateTimeField(blank=False, default=utils.now)
    summary = models.CharField(null=True)
    body = models.TextField(null=True)

    class Meta:
        constraints = [
            # the ~ operator acts as NOT. So check that headline != '' and author != ''
            models.CheckConstraint(check=~models.Q(headline='') & ~models.Q(author=''), name='check_required_fields_non_empty', violation_error_message='Required fields (headline, author) cannot be empty'),
        ]

    def __str__(self) -> str:
        return f"{self.headline} ({self.modified_datetime.date()})"
