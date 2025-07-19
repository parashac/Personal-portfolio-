from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.title
