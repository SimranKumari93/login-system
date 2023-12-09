from django.shortcuts import render, redirect

from . forms import createUserForm, loginFrom

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'auth/index.html')


def register(request):

    form = createUserForm()

    if request.method == "POST":
        form = createUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("login")

    context = {'registerform': form}

    return render(request, 'auth/register.html', context=context)


def login(request):

    form = loginFrom()

    if request.method == 'POST':
        form = loginFrom(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
            
    context = {'loginform': form}

    return render(request, 'auth/login.html', context=context)


def logout(request):

    auth.logout(request)

    return redirect("login")


@login_required(login_url="login")
def dashboard(request):
    return render(request, 'auth/dashboard.html')
