from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def mountains(request):
    queryset=dest_input.objects.filter(dest_category='Mountains')
    context={'destination':queryset}
    return render(request,'dest_input.html',context)

@login_required(login_url='/login/')
def dashboard(request):
    destinations = Destination.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'destinations': destinations})

#view saved destination
@login_required(login_url='/login/')
def save_destination(request):
    if request.method=="POST":
        data=request.POST
        dest_image=request.FILES.get('dest_image')
        dest_desc=data.get('dest_desc')
        dest_tip1=data.get('dest_tip1')
        dest_tip2=data.get('dest_tip2')
        dest_tip3=data.get('dest_tip3')
        title=data.get('title')
        dest_tip4=data.get('dest_tip4')
        dest_tip5=data.get('dest_tip5')

        Destination.objects.create(
            dest_image=dest_image,
            dest_desc=dest_desc,
            dest_tip1=dest_tip1,
            dest_tip2=dest_tip2,
            dest_tip3=dest_tip3,
            dest_title=title,
            dest_tip4=data.get('dest_tip4'),
            dest_tip5=data.get('dest_tip5')
        )
        return redirect('/dashboard/')
    queryset=dest_input.objects.all()
    context={'dashboard':queryset}

    return render(request,'dashboard.html',context)

         # Redirect to the dashboard to view saved destinations

def Temples(request):
    queryset=dest_input.objects.filter(dest_category='Temples')
    context={'destination':queryset}
    return render(request,'dest_input.html',context)

def Forts(request):
    queryset=dest_input.objects.filter(dest_category='Forts')
    context={'destination':queryset}
    return render(request,'dest_input.html',context)

def Picnic(request):
    queryset=dest_input.objects.filter(dest_category='Picnic')
    context={'destination':queryset}
    return render(request,'dest_input.html',context)

@login_required(login_url="/login/")
def destination(request):
    if request.method=="POST":
        data=request.POST
        dest_image=request.FILES.get('dest_image')
        dest_desc=data.get('dest_desc')
        dest_tip1=data.get('dest_tip1')
        dest_tip2=data.get('dest_tip2')
        dest_tip3=data.get('dest_tip3')
        title=data.get('title')
        dest_tip4=data.get('dest_tip4')
        dest_tip5=data.get('dest_tip5')

        dest_input.objects.create(
            dest_image=dest_image,
            dest_desc=dest_desc,
            dest_tip1=dest_tip1,
            dest_tip2=dest_tip2,
            dest_tip3=dest_tip3,
            dest_title=title,
            dest_tip4=data.get('dest_tip4'),
            dest_tip5=data.get('dest_tip5')
        )
        return redirect('/destination/')
    queryset=dest_input.objects.all()
    context={'destination':queryset}

    return render(request,'dest_input.html',context)

def register_page(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=User.objects.filter(username=username)
        if user.exists():
            messages.error(request,'User already exist')
            return redirect('/register/')
        
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()
        messages.info(request,"User Registered Successfully")
        return redirect('/register/')
    return render(request,'register.html')

def login_page(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        # checking if user exists
        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid Username')
            return redirect('/login/')
        #authenticate user
        user=authenticate(username=username,password=password)
        
        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('/login/')
        login(request,user)
        if user.is_staff or user.is_superuser:
            return redirect('/admin/')
        return redirect('/destination/')

    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')
    
