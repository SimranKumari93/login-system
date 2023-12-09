from django.urls import path , include

from . import views

urlpatterns = [
    path('', views.home),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('logout', views.logout, name="logout")
]
