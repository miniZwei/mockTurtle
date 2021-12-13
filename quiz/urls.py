from django.urls import path
from . import views

app_name="QZ"
urlpatterns = [
    path('', views.quiz, name="quiz"),
]