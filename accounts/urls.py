from django.urls import path
from . views import *
from django.contrib.auth import views as auth_views
from . forms import LoginForm

urlpatterns = [
    path('register/', register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('profile/', profile_edit, name='profile'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout', logout, name='logout')
]
