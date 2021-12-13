from django.shortcuts import render

# Create your views here.

def starRating(request):
    return render(request, 'rating/rating.html');
