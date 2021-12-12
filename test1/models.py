from django.db import models

# Create your models here.
class Test(models.Model):
    test_id = models.CharField(max_length=20)