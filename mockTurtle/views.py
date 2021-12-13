from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

def index(request):
    return HttpResponse('index')


def createAccount(request):
    if(request.method == 'POST'):
        username = request.POST.get('username');
        password = request.POST.get('password');
        first_name = request.POST.get('first_name');
        last_name = request.POST.get('last_name');
        email = request.POST.get('email');

        User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
        message = '<script> alert("가입이 완료되었습니다."); document.location.href="/account/login";</script>';
        return HttpResponse(message);

    return render(request, 'registration/register.html')

def myInfo(request):
    if(request.method=='GET'):
        userInfo = User.objects.get(username = (request.user.username));
        context = {
            "userInfo" : userInfo,
        }
        return render(request, 'registration/myinfo.html', context);
    
    else:
         userInfo = User.objects.get(username = (request.user.username));

         password = request.POST.get('password');
         first_name = request.POST.get('first_name');
         last_name = request.POST.get('last_name');
         email = request.POST.get('email');

         if (password != ""):
             userInfo.set_password(password)
         userInfo.first_name = first_name
         userInfo.last_name = last_name
         userInfo.email = email
         userInfo.save()

         return redirect('index')

def deleteInfo(request):
    message = "<script>alert('" + request.user.username + "님이 탈퇴 되었습니다.');"
    message += 'document.location.href="/";</script>'
    User.objects.get(username=(request.user.username)).delete()
    return HttpResponse(message)

def test(request):
    return render(request, 'test.html')

