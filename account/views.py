from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html');




