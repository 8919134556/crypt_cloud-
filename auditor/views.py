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
from data_user.models import Attack_file
from data_user.models import Data_User_Register
from data_owner.models import Upload_file
from data_owner.models import Data_Owner_Register

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def auditor_home(request):
    try:
        request.session["auditor"] == "auditor"
    except:
        return redirect("home")
    return render (request, './auditor/auditor-home.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def revoke(request):
    try:
        request.session["auditor"] == "auditor"
        data = Attack_file.objects.all()

    except:
        return redirect("home")
    return render (request, './auditor/revoke.html', {'view':data})

def auditor_accept(request, email, id):
    accept = get_object_or_404(Data_User_Register, user_email=email)
    accept1 = get_object_or_404(Attack_file, id=id)
    accept.status = 'Accepted'
    accept1.status = 'Accepted'
    email1 = accept.user_email
    accept.save(update_fields = ['status'])
    accept1.save(update_fields = ['status'])
    accept.save()
    email = EmailMessage('Subject',f'Hello {email1},\nHere Your file Details:\nYour Account is Activated Pleas Sign-In', to=[ email1 ])
    email.send()
    messages.success(request, "Activated")
    return redirect ("revoke")

def auditor_revoke(request, email, id) : 
    revoke = get_object_or_404(Data_User_Register, user_email=email)
    revoke1 = get_object_or_404(Attack_file, id=id)
    revoke.status = 'Revoke'
    revoke1.status = 'Revoke'
    email1 = revoke.user_email
    revoke.save(update_fields = ['status'])
    revoke1.save(update_fields = ['status'])
    revoke.save()
    email = EmailMessage('Subject',f'Hello {email1},\nYour Account is Revoked', to=[ email1 ])
    email.send()
    messages.success(request, "Revoked")
    return redirect("revoke")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def trace(request):
    try:
        request.session["auditor"] == "auditor"
        data = Upload_file.objects.all()
    except:
        return redirect("home")
    return render (request, './auditor/trace.html', {'view' : data})

def details(request):
    
    return render (request, './auditor/details.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def auditor_logout(request):
    del request.session["auditor"]
    return redirect("home")