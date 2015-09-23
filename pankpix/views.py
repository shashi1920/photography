from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import Permission,Gallery,Image,Album

# Create your views here.
def homepage(request):
    return render(request,'website/index.html')

def about_us(request):
    return render(request,'website/about_us.html')
def dashboard(request):
    if not request.user.is_authenticated():
        return render(request,'website/denied.html')
    access=Permission.objects.filter(user=request.user)
    GALLERY=Gallery.objects.none()
    for ac in access:
        GALLERY=GALLERY| (Gallery.objects.filter(album=ac.album))


    return render(request,'website/dashboard.html',{'access':access,'gallery':GALLERY})
def gallery(request):
    return render(request,'website/gallery.html')


def contact_us(request):
    return render(request,'website/contact_us.html')
def login_view(request):
    return render(request,'website/login.html')


def contact_mail(request):
    name=request.POST.get('name')
    phone=request.POST.get('phone')
    email=request.POST.get('email')
    message=request.POST.get('message')
    text="<b>A new contact message from a user </b><br>Name: "+name+"<br>Phone: "+phone+"<br>Email: "+email+"<br>"+message
    url='/contact_us/'
    Email='pixelicious.photography@yahoo.com'
    send_mail('Message from a user', text, settings.EMAIL_HOST_USER, [Email], fail_silently=False,html_message=text)
    return HttpResponseRedirect(url)

def logout_user(request):
    if request.user.is_authenticated():
        logout(request)
        state="You have been successfully logged out."
        messages.success(request,state)
    else:
        state="Oops ! You are already logged out ! Try logging in again"
        messages.error(request,state)
    return render(request, 'website/index.html')

def login_user(request):

    username = password = ''
    if request.user.is_authenticated():
        #state="Already logged in, "+request.user.username
        return HttpResponseRedirect('/analytics')
    if request.POST:
        username = request.POST['username']
        password = request.POST['pass']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect('/')
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
            messages.error(request,state)

    return render(request, 'website/index.html')


