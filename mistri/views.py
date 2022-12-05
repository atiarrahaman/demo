from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .forms import MistriuserForm,CustomerUserForm
# Create your views here.
def Login(request):
    if request.method == 'POST':
        fm=AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            username=fm.cleaned_data['username']
            password=fm.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
    else:
        fm=AuthenticationForm()
    context={'form':fm}

    return render(request,'login.html',context)
def Home(request):
    return render(request,'home.html')


def Signup(request):
    if request.method =='POST':
        fm=MistriuserForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('login')
    else:
        fm=MistriuserForm()
    context={'form':fm}
    return render(request,'signup.html',context)
