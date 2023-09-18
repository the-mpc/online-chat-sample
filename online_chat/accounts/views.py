from django.shortcuts import render,redirect
from . import forms as f
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.hashers import make_password
def signin(request):
    message = ""
    if request.method == "POST":
        form = f.SignIn(data=request.POST)
        if form.is_valid():
            form = form.get_user()
            login(request,form)
            return redirect("/")
        else:
            message+="something went wrong! try again later"
    form = f.SignIn()
    return render(request,"signin.html",{"form":form,"message":message})

def signup(request):
    message = ""
    if request.method == "POST":
        form = f.SignUp(request.POST)
        if form.is_valid():
            form = form.save()
            login(request,form)
            return redirect("/")
        else:
            message+="something went wrong! try again later"
    form = f.SignUp()
    return render(request,"signup.html",{"form":form,"message":message})
def signout(request):
    logout(request)
    return redirect("/")