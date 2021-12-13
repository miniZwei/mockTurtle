"""mockTurtle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from quiz.views import quiz
from . import views

app_name="INDEX"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mypage/', include('mypage.urls')),
    path('quiz/', include('quiz.urls')),
    path('', views.index),
    path('bookmark/', include('bookmark.urls')),
    path('achvm/', include('achievement.urls')),
    path('rating/', include('rating.urls')),
    
    path('account/', include('django.contrib.auth.urls')),
    path('account/register/', views.createAccount, name="createAccount"),
    path('account/myinfo/', views.myInfo, name="myInfo"),
    path('account/deleteuser/', views.deleteInfo, name="deleteuser"),

]
