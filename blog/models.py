# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Published')
    heading = models.CharField(max_length=200)
    post_text = models.TextField()
    excerpt = models.TextField()
    heading_image = models.ImageField(upload_to='blog/', max_length=200, default='')
	#content = tinymce_models.HTMLField()
    
    def __str__(self):
        return self.heading