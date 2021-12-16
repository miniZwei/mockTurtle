from django.db import models

# Create your models here.
class Achievement(models.Model):
    achv_no = models.IntegerField(primary_key=True, null=False)
    achv_name = models.CharField(max_length=100, null=False)
    achv_content = models.CharField(max_length=500, null=False)
    achv_condition = models.CharField(max_length=100)
    achv_image = models.CharField(max_length=200)

class AchievementPersonal(models.Model):
    achv_no = models.IntegerField(null=False)
    username = models.CharField(max_length=150, null=False)
    get_date = models.DateField()