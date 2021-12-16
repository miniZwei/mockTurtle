from django.contrib import admin
from rating.models import RatingTotal, RatingPersonal

# Register your models here.
class RatingView(admin.ModelAdmin):
    list_display = ('quiz_no', 'rating_sum', 'rating_avg', 'rating_cnt')

class RatingPSView(admin.ModelAdmin):
    list_display = ('username', 'quiz_no', 'rating_ps')

admin.site.register(RatingTotal, RatingView)
admin.site.register(RatingPersonal, RatingPSView)
