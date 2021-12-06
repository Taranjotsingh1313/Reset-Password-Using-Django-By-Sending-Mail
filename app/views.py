from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render
import uuid
from django.conf import settings
from .models import Profile
from django.core.mail import send_mail
# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username,password=password)
        ftoken = str(uuid.uuid4())
        profile = Profile.objects.create(user=user,forget_token=ftoken)
        if profile and user:
            messages.success(request, 'Profile Created !')
    return render(request,'login.html')

def fpass(request):
    if request.method == 'POST':
        username = request.POST['username']
        user = User.objects.get(username=username)
        print(user.check_password("admin"))
        # profile = Profile.objects.get(user=user)
        # user_email = user.email
        # print(user_email)
        # ftoken = profile.forget_token
        # mail_message = f'Hey Your Reset Password Link is http://127.0.0.1:8000/changepass/{ftoken}/'
        # send_mail('Password Reset Request',mail_message,settings.EMAIL_HOST_USER,[user_email],fail_silently=False)
        # messages.success(request,'MAIL SEND')
    return render(request,'forgetpassword.html')

def changepassword(request,id):
    if request.method == 'POST':
        password = request.POST['password']
        profile = Profile.objects.get(forget_token=id).user
        user = User.objects.get(username=profile)
        user.set_password(password)
        user.save()
        messages.success(request,'Password Changed Please Login! ')
        return redirect('main')
    return render(request,'changepassword.html')

def main(request):
    return render(request,'index.html')