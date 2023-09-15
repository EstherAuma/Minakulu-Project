from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required
def home(request):
    return render(request,'home.html')

@login_required
def data_form(request):
    if request.method == 'POST':
        
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
           
            messages.success(request,'Congratulations, you have been successfully registered' ,extra_tags='bg-success')
            return redirect('home')  
    else:
        form = RegistrationForm()

    return render(request, 'data_form.html', {'form': form})