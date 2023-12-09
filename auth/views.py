from base64 import urlsafe_b64decode
from email.message import EmailMessage
from django.shortcuts import render, redirect
from django.http import HttpResponse 
from . import views as authenticate  
from django.urls import path , include 
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from login import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from . tokens import generate_token
from django.utils.encoding import force_text

# Create your views here.
def home(request):
      return render("authentication/index.html")

def signup(request):
    if request.method == 'POST':
      username = request.POST.get('username')
      fname = request.POST['fname']
      lname = request.POST['lname']
      email = request.POST['email']
      pass1 = request.POST['pass1']
      pass2 = request.POST['pass2']

      if User.objects.filter(username= username):
          messages.error(request, "Username already exists! Please try some other username ")
          return redirect('home')
      if User.objects.filter(email=email):
          messages.error(request, "Email already exists")
          return redirect('home')
      if len(username)>10:
          messages.error(request, "Username must be of 10 character")
          return redirect('home')
      if pass1 != pass2:
          messages.error(request, "Password didn't match")
          return redirect('home')
      if not username.isalnum():
          messages.error(request, "Username must be alphanumeric")
          return redirect('home')
      
      myuser = User.objects.create_user(username, email , pass1)
      myuser.firstname = fname
      myuser.lastname = lname
      myuser.is_active = False
      myuser.save()
      messages.success(request, "Your Account has been created.We have sent you an email please confirm your email and open your account. ")

      ## Welcome Email
      subject = "welcome to gf  - django Login"
      message = "Hello" + myuser.first_name + "! \n " + "Welcome to gfg \n Thank You for visiting ourr website \n we have also sent you a confirmation email, please confirm your email address in order to activate your account. \n\n Thanking You \n "
      from_email = settings.EMAIL_HOST_USER
      to_list = [myuser.email]
      send_mail(subject, message, from_email, to_list, fail_silently=True )

#  Email address Confirmatio Email
      current_site = get_current_site(request)
      email_subject = "Confirm your email @gfg - Django Login !!"
      message2 = render_to_string('email_confirmation.html'), {
          'name': myuser.first_name,
          'domain': current_site.domain,
          'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
          'token': generate_token.make_token(myuser)
      }
      email = EmailMessage(
          email_subject,
          message2,
          settings.EMAIL_HOST_USER,
          [myuser.email],
      )
      email.fail_silently = True
      email.send()

      return redirect('signin')
    
    return render(request, "authentication/signup.html")
def signin(request):
      if request.method == 'POST':
          username = request.POST['username']
          pass1 = request.POST['pass1']
          user = authenticate(username=username, password = pass1)
          if user is not None:
              login(request, user)
              fname = user.firstname
              return render(request, "authentication/index.html", {'fname' : fname, 'lname': lname})
          else:

            messages.error(request, "Bad credentials")
            return redirect('home')
      return render(request, "authentication/signin.html")
def signout(request):
    logout(request)
    messages.success(request,"Logged Out Sucessfully")
    return redirect('home')
      
def activate(request, uidb4, token ):
    try:
        uid = force_text(urlsafe_b64decode(uidb4)) 
        myuser = User.objects(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
       myuser.is_active = True
       myuser.save()
       login(request, myuser)
       return redirect('home')
    else:
        return redirect(request, 'activaton_failed.html')