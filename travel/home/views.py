from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.

def mountains(request):
    queryset=dest_input.objects.filter(dest_category='Mountains')
    context={'destination':queryset}
    return render(request,'dest_input.html',context)

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
