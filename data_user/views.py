from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404,reverse
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.template import loader
from django.shortcuts import render
from cryptography.fernet import Fernet, MultiFernet
import requests
from data_owner.models import Upload_file
from django.utils.crypto import get_random_string
from django.core.mail import EmailMessage
from django.views.decorators.cache import cache_control
import pathlib 
from .models import *
import os.path


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def data_user(request):
    try :
        data = Data_User_Register.objects.get(user_email= request.session["data_user_email"])
        demo = data.user_image
        demo1 = data.user_name
    except:
        return redirect("home")
    return render(request, './data-user/data-user.html', {'view': demo, 'view1' : demo1})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def search_files(request):
    try :
        data = Data_User_Register.objects.get(user_email=request.session["data_user_email"])
        demo = data.user_image
        demo1 = data.user_email
        data1 = Upload_file.objects.filter(select="Public",status="Accepted")
        data2 = Request_file.objects.filter(request_mail = request.session["data_user_email"])

    except:
        return redirect("home")
    return render (request, './data-user/search-file.html', {'view': demo, 'view2' : demo1, 'view1' : data1, 'view3': data2})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def file_request(request,id, email):
    request = get_object_or_404(Upload_file, id=id)
    file_id = request.id
    file_name =request.file_name 
    file_type = request.file_type
    file_size = request.file_size
    owner_id = request.owner_id
    file_location = request.files
    key = request.Key
    files = Request_file.objects.create(file_id=file_id, file_name=file_name, file_type=file_type, file_size=file_size, request_mail=email, owner_id=owner_id, Key = key, user_file = file_location)
    files.save()
    return redirect("search_files")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def my_download(request):
    try :
        data = Data_User_Register.objects.get(user_email=request.session["data_user_email"])
        demo = data.user_image
        
        
        data2 = Request_file.objects.filter(request_mail = request.session["data_user_email"])
    except:
        return redirect("home")

    return render (request, './data-user/my-download.html', {'view': demo, 'view3': data2})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def my_pro(request):
    try :
        data = Data_User_Register.objects.get(user_email=request.session["data_user_email"])
        demo = data.user_image
    except:
        return redirect("home")
    return render (request, './data-user/my-profile.html', {'view': demo, 'view1': data})


def download(request):
    try :
        data = Data_User_Register.objects.get(user_email=request.session["data_user_email"])
        demo = data.user_image
        context = {'view': demo}
         
        if request.method == "POST" :
            screat_key = request.POST['screat_key']
            post_key = request.POST['key']
            
            k = Request_file.objects.get(screat_key=screat_key)
            print(k)
            key = k.Key
            sec_key = k.screat_key
            filename = k.user_file
            u_email = k.request_mail
            f_name = k.file_name
            f_size = k.file_size

            print(u_email)
            
            print(filename)
            E= os.path.basename(f'{filename}')
            print(E)

            if key == post_key and screat_key == sec_key :
                if u_email == request.session["data_user_email"]:

                    k = Fernet(key)
                    path = (settings.MEDIA_ROOT).replace('\\', '/')
                    print(path)
                    data1 = (path+"/" +f'{filename}')
                    print(data1)
                    obj = open(data1).read()
                    ob = bytes(obj, 'utf-8')
                    files = k.decrypt(ob).decode()
                    download_files = Download_file.objects.create(user_email=u_email, file_name=f_name, file_size=f_size)
                    download_files.save()
                

                    context={
                        'view2' : E,
                        'view1' : files,
                        'view': demo
                    }
                else:
                    user_name = data.user_name
                    user_email = data.user_email
                    user_image = data.user_image
                    attack_file =  f_name
                    attack_file = Attack_file.objects.create(user_name=user_name, user_email=user_email, user_image=user_image,attack_file=attack_file)
                    attack_file.save()
                    messages.error(request, "Your Account is Hold")
                    del request.session["data_user_email"]
                    return redirect("home")
            else:
                messages.error(request, "key Does Not Match")
    except:
        pass
    return render (request, './data-user/download.html', context=context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def user_logout(request):
    del request.session["data_user_email"]
    return redirect("home")