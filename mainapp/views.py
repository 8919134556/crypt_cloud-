from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404,reverse
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.template import loader
# Create your views here.
from data_user.models import Data_User_Register
from data_owner.models import Data_Owner_Register
from django.shortcuts import render

def home(request):
    return render (request, './main/index.html')

def about(request):
    return render (request, './main/about.html')

def contact(request):
    return render (request, './main/contact.html')

def cloud(request):
    if request.method == "POST":
        email = request.POST.get('username')
        pws = request.POST.get ('pass')
        if email =='cloud' and pws =='cloud':
            request.session["cloud"]= email
            messages.success(request, "welcome")
            return redirect('dashboard')
            
        else:
            messages.error(request, "bad credential Please Register")
            return redirect('cloud')
    return render (request, './main/cloud.html')

def authority(request):
    if request.method == "POST":
        admin_email = request.POST.get('userName')
        admin_pws = request.POST.get ('pass')
        if admin_email =='authority' and admin_pws =='authority':
            request.session["admin_email"]= admin_email
            messages.success(request, "welcome")
            return redirect('authority_home')
            
        else:
            messages.error(request, "bad credential Please Register")
            return redirect('authority')
    return render(request, './main/authority.html')

def auditor(request):
    if request.method == "POST":
        email = request.POST.get('username')
        pws = request.POST.get ('pass')
        if email =='auditor' and pws =='auditor':
            request.session["auditor"]= email
            messages.success(request, "welcome")
            return redirect('auditor_home')
            
        else:
            messages.error(request, "bad credential Please Register")
            return redirect('auditor')
    return render (request, './main/auditor.html')

def data_owner_reg(request):
    if request.method == "POST" and request.FILES["image"]  :
        fname = request.POST['name']       
        gender = request.POST['inlineRadioOptions']
        phone = request.POST['phone']
        image = request.FILES['image']
        email = request.POST['email']
        password = request.POST['pass']
        try:
            
            if  Data_Owner_Register.objects.filter(user_phone=phone).exists():
                messages.error (request, "Phone Number alredy exist")
            elif  Data_Owner_Register.objects.filter(user_email=email).exists():
                messages.error (request, "Email alredy exist")
            else:
                reg_details = Data_Owner_Register.objects.create(user_name=fname,user_phone=phone,gender=gender,user_email=email,user_pwd=password, user_image = image)
                reg_details.save()
                messages.success(request, "Resgistration successfully Done")
                return redirect("data_owner_login") 
        
        except:
            pass
    return render (request, './main/data-owner-register.html')

def data_user_reg(request):
    if request.method == "POST" and request.FILES["image"]  :
        fname = request.POST['fname']
        lname = request.POST['lname']
        gender = request.POST['inlineRadioOptions']
        dob = request.POST['dob']
        phone = request.POST['phone']
        image = request.FILES['image']
        email = request.POST['email']
        password = request.POST['pass']
        try:
            
            if  Data_User_Register.objects.filter(user_phone=phone).exists():
                messages.error (request, "Phone Number alredy exist")
            elif  Data_User_Register.objects.filter(user_email=email).exists():
                messages.error (request, "Email alredy exist")
            else:
                reg_details = Data_User_Register.objects.create(user_name=fname,user_lastname=lname,user_phone=phone,gender=gender,date_of_birth=dob,user_email=email,user_pwd=password, user_image = image)
                reg_details.save()
                messages.success(request, "Resgistration successfully Done")
                return redirect("data_user_login") 
        
        except:
            pass
    return render (request, './main/data-user-register.html')

def data_owner_login (request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('pass')
        try:
            login = Data_Owner_Register.objects.get(user_email=email,user_pwd=password)
            acc = login.status
            if acc == "Accepted":
                request.session["data_owner_email"]=login.user_email
                return redirect ("data_owner")
            else:
                messages.error(request, "Your Account is not Activated")

        except:
            messages.error(request, "bad credential Please Register")
            return redirect("data_owner_login")
    return render (request, './main/data-owner-login.html')

def data_user_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('pass')
        try:
            login = Data_User_Register.objects.get(user_email=email,user_pwd=password)
            acc = login.status
            if acc == "Accepted":
                request.session["data_user_email"]=login.user_email
                return redirect ("data_user")
            elif acc == "Revoke":
                messages.error(request, "Your Account is Revoked")
            else:
                messages.error(request, "Your Account is not Activated")

        except:
            messages.error(request, "bad credential Please Register")
            return redirect("data_user_login")
    return render (request, './main/data-user-login.html')


