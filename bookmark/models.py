from django.db import models

# Create your models here.
class Bookmark(models.Model):
    username = models.CharField(max_length=150, null=False)
    quiz_no = models.IntegerField(null=False, blank=False)
    