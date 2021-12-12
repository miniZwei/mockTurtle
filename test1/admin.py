from django.contrib import admin
from test1.models import Test

# Register your models here.
class TestView(admin.ModelAdmin):
    list_display=('id', 'test_id')

admin.site.register(Test, TestView)