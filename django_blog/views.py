from django.shortcuts import render, redirect

# Create your views here.

def home(request):
	return redirect('posts:list')