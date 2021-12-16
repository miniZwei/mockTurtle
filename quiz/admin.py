from django.contrib import admin
from quiz.models import Quiz

# Register your models here.
class QuizView(admin.ModelAdmin):
    list_display = ('quiz_no', 'quiz_title')

admin.site.register(Quiz, QuizView)