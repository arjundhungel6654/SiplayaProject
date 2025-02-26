from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.

date=datetime.now()
  
def index(request):
  if request.method=="POST":
        data=request.POST
        name=data['name']
        email=data['email']
        subject=data['subject']
        level=data['level']
        message=data['message'] 
        user=Student(name=name,email=email,subject=subject,level=level,message=message)
        user.save()
        messages.success(request,f'hi  {name}  your data is submited')
        return redirect('index')

  return render(request,'app/index.html')


def coursedetails(request):
  return render(request,'app/coursedetails.html')

def teams(request):
  return render(request,'app/teams.html')

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST["email"]
        password=request.POST['password']
        password1=request.POST['password1']

        if password==password1:
            try:
                validate_password(password)
                if User.objects.filter(username=username).exists():
                    messages.error(request,"username already exists")
                    return redirect("register")
                if User.objects.filter(email=email).exists():
                    messages.error(request,"Email already exists")
                    return redirect("register")
                User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                
                messages.success(request,'your account is successfully registered')
                
                return redirect('log_in')
            except ValidationError as e:
                for error in e.messages:
                    messages.error(request,error)
            return redirect("register")
        else:
            messages.error(request,"your password does not match")
            return redirect('register')

    return render(request,'auth/register.html')


def log_in(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        if not User.objects.filter(username=username).exists():
            messages.error(request,'username doesnot exists')
            return redirect('log_in')
        
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request,'your password is incorrect!!!')
            return redirect('log_in')

    return render(request,'auth/login.html')    

def log_out(request):
    logout(request)
    return redirect('log_in')

@login_required(login_url='log_in')
def change_password(request):
    form=PasswordChangeForm(user=request.user)
    if request.method=='POST':
        form=PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
         form.save()
        return redirect('log_in')
    return render(request,'auth/change_password.html',{'form':form})