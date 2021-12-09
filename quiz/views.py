from django.shortcuts import render, HttpResponse

# Create your views here.
def quiz(request):
    return render(request, 'quiz/quiz.html')
