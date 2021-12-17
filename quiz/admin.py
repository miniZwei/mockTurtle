from django.contrib import admin
from quiz.models import Quiz, SolvedQuiz

# Register your models here.
class QuizView(admin.ModelAdmin):
    list_display = ('quiz_no', 'quiz_title')

admin.site.register(Quiz, QuizView)

class SolvedQuizView(admin.ModelAdmin):
    list_display = ('username', 'quiz_no')

admin.site.register(SolvedQuiz, SolvedQuizView)