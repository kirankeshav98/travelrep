from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials!")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email=request.POST['email']
        pw=request.POST['password']
        cpw=request.POST['confirm_password']
        if pw==cpw:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already taken.Try another")
                return redirect ('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already taken.Try another")
                return redirect ('register')
            else:
                user=User.objects.create_user(username=username,password=pw,first_name=firstname,last_name=lastname,email=email)
                user.save()
                print('user created')
        else:
            messages.info(request,"Password mismatching.Try again")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')