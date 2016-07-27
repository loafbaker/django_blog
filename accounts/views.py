from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.

from .forms import UserLoginForm, UserRegisterForm


def login_view(request):
	title = 'Login'
	next = request.GET.get('next', 'home')
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		login(request, user)
		# TODO: Redirect to the user main console
		messages.success(request, 'The user has logged in successfully.')
		return redirect(next)
	context = {
		'title': title,
		'form': form,
	}
	return render(request, 'form.html', context)

def register_view(request):
	title = 'Register'
	next = request.GET.get('next', 'home')
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		my_user = authenticate(username=user.username, password=password)
		login(request, my_user)
		# TODO: Return a message and redirect to another page
		messages.success(request, 'New user has been registered successfully.')
		return redirect(next)
	context = {
		'title': title,
		'form': form,
	}
	return render(request, 'form.html', context)

def logout_view(request):
	logout(request)
	messages.success(request, 'The user has logged out successfully.')
	return redirect('home')