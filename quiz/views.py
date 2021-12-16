from django.shortcuts import render, HttpResponse

from quiz.models import Quiz

# Create your views here.
def quiz(request):
    quiz = Quiz.objects.get(quiz_no = 1)
    print(quiz.quiz_title)
    context = {
        'quiz' : quiz,
    }
    return render(request, 'quiz/quiz.html', context)
