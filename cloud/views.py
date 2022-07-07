from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404,reverse
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.template import loader
from django.shortcuts import render
from cryptography.fernet import Fernet, MultiFernet
import requests
from django.utils.crypto import get_random_string
from django.core.mail import EmailMessage
from django.views.decorators.cache import cache_control
import pathlib 
from data_user.models import Data_User_Register
from data_owner.models import Upload_file
from data_owner.models import Data_Owner_Register
from data_user.models import Request_file
from data_user.models import Attack_file

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dashboard(request):
    
    try:
        request.session["cloud"] == "cloud"
        data = Upload_file.objects.all().count()
        data1 = Data_Owner_Register.objects.all().count()
        data2 = Data_User_Register.objects.all().count()
        data3 = Request_file.objects.all().count()
        
        print("1")
        context = {
            'view' : data,
            'view1' : data1,
            'view2' : data2,
            'view3' : data3
            
            }
    except:
        return redirect("home")
    
    return render(request, './cloud/dashboard.html', context=context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def d_owner(request):
    try:
        request.session["cloud"] == "cloud"
        data = Data_Owner_Register.objects.all()
    except:
        return redirect("home")
    return render(request, './cloud/data-owner.html', {'view':data})

def owner_accept(request, id):
    accept = get_object_or_404(Data_Owner_Register, id=id)
    accept.status = 'Accepted'
    email = accept.user_email
    accept.save(update_fields = ['status'])
    accept.save()
    email = EmailMessage('Subject',f'Hello {email},\nHere Your file Details:\nYour Account is Activated Pleas Sign-In', to=[ email ])
    email.send()
    messages.success(request, "Accepted")
    return redirect ("d_owner")

def owner_reject(request, id) : 
    reject = get_object_or_404(Data_Owner_Register, id=id)
    reject.status = 'Rejected'
    email = reject.user_email
    reject.save(update_fields = ['status'])
    reject.save()
    email = EmailMessage('Subject',f'Hello {email},\nYour Account is Rejected try another way', to=[ email ])
    email.send()
    messages.success(request, "successfuly rejected")
    return redirect("d_owner")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def d_user(request):
    try:
        request.session["cloud"] == "cloud"
        data = Data_User_Register.objects.all()
    except:
        return redirect("home")
    return render (request, './cloud/data-user.html', {'view' : data})

def user_accept(request, id):
    accept = get_object_or_404(Data_User_Register, id=id)
    accept.status = 'Accepted'
    email = accept.user_email
    accept.save(update_fields = ['status'])
    accept.save()
    email = EmailMessage('Subject',f'Hello {email},\nHere Your file Details:\nYour Account is Activated Pleas Sign-In', to=[ email ])
    email.send()
    messages.success(request, "Accepted")
    return redirect ("d_user")

def user_reject(request, id) : 
    reject = get_object_or_404(Data_User_Register, id=id)
    reject.status = 'Rejected'
    email = reject.user_email
    reject.save(update_fields = ['status'])
    reject.save()
    email = EmailMessage('Subject',f'Hello {email},\nYour Account is Rejected try another way', to=[ email ])
    email.send()
    messages.success(request, "successfuly rejected")
    return redirect("d_user")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def data_access(request):
    try:
        request.session["cloud"] == "cloud"
        data = Upload_file.objects.all()
    except:
        return redirect("home")
    return render (request, './cloud/data-access.html', {'view': data})

def data_accept(request, id):
    accept = get_object_or_404(Upload_file, id=id)
    accept.status = 'Accepted'
    email = accept.owner.user_email
    accept.save(update_fields = ['status'])
    accept.save()
    email = EmailMessage('Subject',f'Hello {email},\nHere Your file is Accepted', to=[ email ])
    email.send()
    messages.success(request, "Accepted")
    return redirect ("data_access")

def data_reject(request, id) : 
    reject = get_object_or_404(Upload_file, id=id)
    reject.status = 'Rejected'
    email = reject.owner.user_email
    reject.save(update_fields = ['status'])
    reject.save()
    email = EmailMessage('Subject',f'Hello {email},\nYour file is Rejected try another way', to=[ email ])
    email.send()
    messages.success(request, "successfuly rejected")
    return redirect("data_access")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def cloud_logout(request):
    del request.session["cloud"]
    return redirect("home")