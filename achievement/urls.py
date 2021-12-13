from django.urls import path, re_path
from . import views


app_name = "ACHV"

urlpatterns = [

path('', views.achvm, name="achvList"),

]
