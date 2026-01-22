from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from . models import *
from . forms import *
from django.contrib.auth.decorators import login_required

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Account Were Created Successfully")
            return redirect('login')
    context = {
        "form":form
    }
    return render(request, "register.html", context)

@login_required
def profile_edit(request):
    user_form = UserUpdateForm(request.POST or None, instance=request.user)
    profile_form = ProfileForm(request.POST or None, request.FILES or None, instance=request.user.profile)

    if user_form.is_valid() and profile_form.is_valid():
        user_form.save()
        profile_form.save()
        messages.success(request, "Profile Will Edit Successfully")
        return redirect('dashboard')

    return render(request, 'profile_edit.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def logout(request):
    auth_logout(request)
    messages.success(request, "You Logout Successfully")
    return redirect('login')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')