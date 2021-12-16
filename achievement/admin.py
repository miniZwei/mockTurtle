from django.contrib import admin
from achievement.models import Achievement, AchievementPersonal

# Register your models here.
class AchievementView(admin.ModelAdmin):
    list_display = ('achv_no', 'achv_name', 'achv_condition')

class AchievementPersonalView(admin.ModelAdmin):
    list_display = ('achv_no', 'username', 'get_date')

admin.site.register(Achievement, AchievementView)
admin.site.register(AchievementPersonal, AchievementPersonalView)

