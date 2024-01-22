from django.shortcuts import render,redirect

# Create your views here.
from .forms import UserRegisterForm,UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


from django.contrib import messages

def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'],cd['password'])
            messages.success(request,'your registration successful')
            return redirect('home')

    else :
        form = UserRegisterForm()
    return render(request, 'register.html',{'form':form})
    

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user= authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request,'login successfully', 'success')
                return redirect('home')
            else:
                messages.error(request,'user or pass is not valid !', 'danger')
                
    else :
        form = UserLoginForm()
    return render(request, 'login.html',{'form':form})



def userlogout(request):
    logout(request)
    messages.success(request,'logout successfully','success')
    return redirect('home')

