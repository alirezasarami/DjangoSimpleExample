import email
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from sharif.log_require import log

def login(request):
    return render(request,'login.html' )
@log
def logout(request):
    auth.logout(request)
    return render(request,'logout.html')

@log
def register(request):
    return render(request,'register.html')

@log
def save_user(request):
    user = request.POST['user']
    passw = request.POST['passw']
    email = request.POST['email']
    user_obj = User.objects.create_user(user,email,passw)
    user_obj.is_active = False
    user_obj.save()
    return HttpResponse('user saved')

#solution 2

@login_required(login_url='/user/login/')
@log
def show_profile(request):
    #solution 1
    if request.user.is_authenticated:
        username = request.user.username
        firstname = request.user.first_name
        lastname = request.user.last_name
        email = request.user.email
        return render(request,'show_profile.html',{'uname':username , 'fname': firstname , 'lname':lastname , 'email':email})   
    else:
        return render(request , 'login.html')

def show_home(request):
    if auth.authenticate(username = request.POST['user'] , password = request.POST['passw']):
        userObject = auth.authenticate(username = request.POST['user'] , password = request.POST['passw'])
        auth.login(request, userObject)
        print(request.user)
        username = request.user.username
        return render(request , 'home.html' , {'Uname' : username}) 
    else:
        return HttpResponse('faild')

@login_required(login_url='/user/login/')
@log
def edit_prifile(request):
    uname = request.user.username
    fname = request.POST['firstname']
    lname  = request.POST['lastname']
    mail = request.POST['email']

    User.objects.filter(username = uname).update(first_name = fname , last_name = lname , email = mail)
    return HttpResponse('saved!')
# from django
# Create your views here.
 