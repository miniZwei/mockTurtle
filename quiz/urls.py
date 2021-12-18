from django.urls import path, re_path
from . import views

app_name="QZ"
urlpatterns = [
    path('<quiz_no>/', views.quiz, name="quiz"),

]