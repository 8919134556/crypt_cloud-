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
from data_user.models import Request_file

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def authority_home(request):
    try:
        if (request.session["admin_email"] == "authority"):
            data = Request_file.objects.filter(status = "Pending")
        else:
            pass
    except:
        return redirect("home")
    return render (request, './authority/authority-home.html', {'view':data})

def accept(request, id):
    accept = get_object_or_404(Request_file, id=id)
    accept.status = 'Accepted'
    email = accept.request_mail
    key = accept.Key
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    demo = get_random_string(6, chars)
    accept.screat_key = demo
    accept.save(update_fields = ['status', 'screat_key'])
    accept.save()
    email = EmailMessage('Subject',f'Hello {email},\nHere Your file Details:\nYour Screte Key No : {demo}\n File Key : {key}', to=[ email ])
    email.send()
    messages.success(request, "Activated")
    return redirect ("authority_home")

def reject(request, id) : 
    reject = get_object_or_404(Request_file, id=id)
    reject.status = 'Rejected'
    email = reject.request_mail
    reject.save(update_fields = ['status'])
    reject.save()
    email = EmailMessage('Subject',f'Hello {email},\nYour Request is Rejected try another way', to=[ email ])
    email.send()
    messages.success(request, "successfuly deactivated")
    return redirect("authority_home")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def authority_logout(request):
    del request.session["admin_email"]
    return redirect("home")