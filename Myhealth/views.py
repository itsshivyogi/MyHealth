from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render
from django.template.loader import get_template
from django.contrib import messages
from .forms import 	SignUpForm, LoginForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password1']
            if not (User.objects.filter(username=username).exists() and User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                if user is not None:		
                    if user.is_active:
                        login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = SignUpForm()
    return render(request, 'templates/signup.html', {'form' : form})
	
def mylogin(request):
    logout(request)
    username = password = ''
    print("Hello")
    if request.POST:
        uname = request.POST.get('username', '')
        pwd = request.POST.get('password', '')

        print(uname + "  " + pwd)
        user = authenticate(username=uname, password=pwd)
        if user is not None:		
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('home.html')		
    else:
        print("Login Started")
        context = {
        }
        template = get_template('templates/login.html')
        return HttpResponse(template.render(context, request))

def mylogout(request):
    logout(request)
    print("Logout!!!")
    return HttpResponseRedirect("login.html")

	
def home(request):
    template = get_template('templates/home.html')
    currentuser = request.user
    print("Current user  ")
    print(currentuser)
    context = {
        'user': currentuser,
    }
    return HttpResponse(template.render(context, request))
		

def food(request):
    currentuser = request.user
    print("Food : Current user  ")
    print(currentuser)
    if request.POST:
        print("POST")
        return HttpResponseRedirect('home.html')		
    else:
        template = get_template('templates/food.html')
        context = {
	    'user': currentuser,
        }
        return HttpResponse(template.render(context, request))
