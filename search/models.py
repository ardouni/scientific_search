from django.db import models

class ScientificPaper(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    abstract = models.TextField()
    keywords = models.CharField(max_length=255)

    def __str__(self):
        return self.title
