from django.urls import path, re_path
from . import views


app_name = "BM"

urlpatterns = [

path('', views.bookmark, name="bmark"),

]
