from django.shortcuts import render, redirect
from rating.models import RatingPersonal
from quiz.models import Quiz

# Create your views here.

def starRating(request):
    if request.method == 'GET':
        rptable = RatingPersonal.objects.get(username = request.user.username)
        quiz = Quiz()

        context = {
            'rp' : rptable,
            'quiz' : quiz
        }

        return render(request, 'rating/rating.html', context);