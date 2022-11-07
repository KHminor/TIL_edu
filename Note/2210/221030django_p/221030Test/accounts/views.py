from django.shortcuts import render, redirect
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model, get_user, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm



# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('movies:index')

    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('movies:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movies:index')

    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('movies:index')


def delete(request):
    if request.user.is_authenticated:
        request.user.delete()    
        auth_logout(request)
    return redirect('movies:index')


def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('movies:index')

    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('movies:index')

    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/change_password.html', context)


def profile(reqeust, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {
        'person' : person,
    }
    return render(reqeust,'accounts/profile.html', context)


def follow(request, user_pk):
    if request.user.is_authenticated:
        User = get_user_model()
        me = request.user
        you = User.objects.get(pk=user_pk)

        if me != you:
            # 내가 (request.user) 그 사람의 팔로워 목록에 있다면
            # if me in you.followers.all():
            if you.followers.filter(pk=me.pk).exists():
                # 언팔로우
                you.followers.remove(me)
            else:
                # 팔로우
                you.followers.add(me)
        return redirect('accounts:profile', you.username)
    return redirect('accounts:login')