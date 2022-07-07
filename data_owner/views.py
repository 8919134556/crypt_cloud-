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
from .models import *

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def data_owner (request):
    try:
        data = Data_Owner_Register.objects.get(user_email=request.session["data_owner_email"])
        demo = data.user_image
        demo1 = data.user_name
    except:
        return redirect("home")
    return render (request, './data-owner/data-owner.html', {'view': demo, 'view1' : demo1})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def data_upload(request):
    try :
        data = Data_Owner_Register.objects.get(user_email=request.session["data_owner_email"])
        demo1 = data.id
        demo2 = data.user_image
        if request.method == "POST" and request.FILES["file1"]  :
            name = request.POST['name']
            decription = request.POST['decription']
            select = request.POST['inlineRadioOptions']
            filename = request.FILES['file1']
            size = request.POST['size']
            file_type = pathlib.Path(f'{filename}').suffix
            file_data = "none"
            key = str(Fernet.generate_key(), 'utf-8')
            crypter = Fernet(key)
            upload_file = Upload_file.objects.create(owner_id=demo1,decription=decription,files = filename,
            file_name=name, file_type=file_type, file_size=size, Key=key, file_data=file_data, select=select)
            upload_file.save()
            data = (settings.MEDIA_ROOT+"\\User\\Files\\")
            data1 = (data +f'{filename}')
            obj = open(data1, 'r')
            demo1 = obj.read()
            datafile = demo1.encode()
            files = str(crypter.encrypt(datafile), 'utf-8')
            f = open (data1, 'w')
            f.write(files)
            d = Upload_file.objects.get(Key=key)
            d.file_data = files
            d.save()
            f.close()
            messages.success(request, "successfully Done")
    except:
        return redirect("home")
    return render (request, './data-owner/data-upload.html', {'view': demo2})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def view_files(request):
    try:
        data = Data_Owner_Register.objects.get(user_email=request.session["data_owner_email"])
        demo = data.user_image
        demo1 = data.id
        data1 = Upload_file.objects.filter(owner_id=demo1)
    except:
        return redirect("home")
    
    return render (request, './data-owner/view-files.html', {'view': demo, 'view1' : data1})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def profile(request):
    try :
        data = Data_Owner_Register.objects.get(user_email=request.session["data_owner_email"])
        demo = data.user_image
    except:
        return redirect("home")
    return render (request, './data-owner/profile.html', {'view': demo, 'view1': data})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    del request.session["data_owner_email"]
    return redirect("home")