"""
Auth views
"""
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.http import url_has_allowed_host_and_scheme
from django import forms
from .models import User


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}))

    class Meta:
        model = User
        fields = ['email', 'username']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('A user with that email already exists.')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('That username is already taken.')
        return username

    def clean(self):
        cleaned = super().clean()
        if cleaned.get('password') != cleaned.get('password_confirm'):
            raise forms.ValidationError("Passwords don't match")
        return cleaned

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


def get_safe_redirect_url(request, next_url, default='/dashboard/'):
    if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}, require_https=request.is_secure()):
        return next_url
    return default


def login_view(request):
    next_url = request.POST.get('next') or request.GET.get('next', '')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(get_safe_redirect_url(request, next_url))
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form, 'next': next_url})


def register_view(request):
    next_url = request.POST.get('next') or request.GET.get('next', '')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(get_safe_redirect_url(request, next_url))
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form, 'next': next_url})


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')
