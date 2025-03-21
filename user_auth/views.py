from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def signup_user(request):
    context = {}
    if request.method == 'POST':
        uname = request.POST.get('uname','')
        pwd1 = request.POST.get('pwd1','')
        pwd2 = request.POST.get('pwd2','')
        if pwd1 == pwd2:
            if not User.objects.filter(username = uname):
                User.objects.create_user(
                    username = uname,
                    password = pwd1,
                )
                return redirect('login')
            else:
                context['error'] = 'User already exists !!!'
        else:
            context['error'] = " Passwords doen't match"
            
        
    return render(request,'signup.html',context) 

def login_user(request):
    context = {}
    if request.method == 'POST':
        uname = request.POST.get('uname','')
        pwd = request.POST.get('pwd','')
        user = authenticate(request, username = uname, password = pwd)
        if user is not None:
            login(request,user)
            return redirect('articles-list')
        else:
            context['error'] = 'Invalid Credentials'
    return render(request,'login.html',context)

def logout_user(request):
    logout(request)
    return redirect('login')