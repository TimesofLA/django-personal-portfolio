from django.db import models
from ckeditor.fields import RichTextField


class Blog(models.Model):
    title = models.CharField(max_length=162)
    date = models.DateField()
    description = RichTextField(blank=True, null=True)
    # description = models.TextField()

    def __str__(self):
        return self.title
