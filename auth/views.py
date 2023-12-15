from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import createUserForm, loginFrom
from . models import Feature 
from django.contrib import messages 
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.details = 'our service is very quick'

    feature2 = Feature()
    feature2.id = 0
    feature2.name = 'Fast'
    feature2.details = 'our service is very quick'

    feature3 = Feature()
    feature3.id = 0
    feature3.name = 'Fast'
    feature3.details = 'our service is very quick'

    feature4 = Feature()
    feature4.id = 0
    feature4.name = 'Fast'
    feature4.details = 'our service is very quick'
    
     
    return render(request, 'index.html',{ 'feature' : feature1})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
           if User.objects.filter(email= email).exists():
               messages.info(request, 'Email already exists')
               return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.info(request, "Username already exists")
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save();
            return redirect('login') 
    else:
        messages.info(request, "password didn't match")
        return redirect('register') 
    # else: 
    # return redirect('/')  
 
    return render(request , 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username= username, password=password)
        if user is not None :
            auth.login(request, user)
        return redirect('/')
    else:
        messages.info(request, 'Invalid Credentials')
        return redirect('login')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
def counter(request):
    text = request.GET['text']
    amount_of_words = len(text.split())
    return render(request, 'auth/counter.html', {'amount': amount_of_words})

# def home(request):
#     return render(request, 'auth/index.html')


# def register(request):

#     form = createUserForm()

#     if request.method == "POST":
#         form = createUserForm(request.POST)

#         if form.is_valid():
#             form.save()

#             return redirect("login")

#     context = {'registerform': form}

#     return render(request, 'auth/register.html', context=context)


# def login(request):

#     form = loginFrom()

#     if request.method == 'POST':
#         form = loginFrom(request, data=request.POST)

#         if form.is_valid():
#             username = request.POST.get('username')
#             password = request.POST.get('password')

#             user = authenticate(request, username=username, password=password)

#             if user is not None:
#                 auth.login(request, user)
#                 return redirect("dashboard")
            
#     context = {'loginform': form}

#     return render(request, 'auth/login.html', context=context)


# def logout(request):

#     auth.logout(request)

#     return redirect("login")


# @login_required(login_url="login")
# def dashboard(request):
#     return render(request, 'auth/dashboard.html')
