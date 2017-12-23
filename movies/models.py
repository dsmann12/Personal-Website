from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Review(models.Model):
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Published')
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(default='')
    excerpt = models.TextField()
    heading_image = models.ImageField(upload_to='blog/', max_length=200, default='')

    def __str__(self):
        return self.title
