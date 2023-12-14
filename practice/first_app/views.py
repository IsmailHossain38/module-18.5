from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate, login,logout ,update_session_auth_hash
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else: 
        form = RegistrationForm()
    return render(request,'register.html', {"form": form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            
            name=form.cleaned_data['username']
            userpass=form.cleaned_data['password']
            user = authenticate(username=name , password =userpass)
            if user is not None:
                messages.success(request,'Login user successfully !')
                login(request,user)
                return redirect('profile')
                
    else: 
        form = AuthenticationForm(request.POST)
    return render(request,'register.html', {"form": form})
@login_required  
def user_changepass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
        form=PasswordChangeForm(user=request.user)
    return render(request,'change_pass.html',{'form':form})
@login_required  
def user_changepass2(request):
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
        form=SetPasswordForm(user=request.user)
    return render(request,'change_pass.html',{'form':form})
    
@login_required
def user_logout(request):
    logout(request)
    messages.info(request,"LogOut successfully!")
    return redirect('register')
@login_required
def profile(request):
    return render(request,'profile.html')