from django.db import models

# Create your models here.
class RatingTotal(models.Model):
    quiz_no = models.IntegerField(primary_key=True, null=False)
    rating_sum = models.IntegerField()
    rating_avg = models.IntegerField()
    rating_cnt = models.IntegerField()

class RatingPersonal(models.Model):
    username = models.CharField(max_length=150, null=False)
    quiz_no = models.IntegerField(null=False)
    rating_ps = models.IntegerField()
