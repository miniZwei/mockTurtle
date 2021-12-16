from django.urls import path, re_path
from . import views


app_name = "RT"

urlpatterns = [
    path('', views.starRating, name="SR"),
    path('test/', views.test)
]
