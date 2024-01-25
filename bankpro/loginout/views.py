from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Exists !')
                return redirect('LoginOut:register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'UserName Already Exists !')
                return redirect('LoginOut:register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                print('User Created ')
                return redirect('LoginOut:login')
        else:
            messages.info(request, 'Password Does Not Match !')
            return redirect('LoginOut:register')

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('LoginOut:formindex')
        else:
            messages.info(request, 'INVALID USERNAME OR PASSWORD')
            return redirect('LoginOut:login')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def form(request):

    return render(request, 'form.html')


def formindex(request):
    return render(request, 'formindex.html')

