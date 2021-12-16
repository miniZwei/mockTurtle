from django.shortcuts import render

# Create your views here.

def bookmark(request):
    return render(request, 'bookmark/bookmark.html');

def bmtest(request):
    return render(request, 'bookmark/bmtest.html');
