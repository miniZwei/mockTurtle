from django.shortcuts import render, redirect
from rating.models import RatingPersonal

# Create your views here.

def starRating(request):
    return render(request, 'rating/rating.html');

def test(request):
    if request.method == 'POST':
        rptable = RatingPersonal()
        rptable.username = request.user.username
        rptable.quiz_no = 999
        rptable.rating_ps = request.POST.get('rating_ps')
        rptable.save()

        return redirect('/mypage/')
    
    else:
        return render(request, 'rating/test.html')