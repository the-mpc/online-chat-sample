from django.shortcuts import render
from chat import forms as f
from chat import models as db
from django.contrib.auth.decorators import login_required
@login_required()
def home(request):
    form = f.SearchForm()
    rooms = db.Room.objects.filter(created_by=request.user)
    return render(request,"home.html",{"form":form,"rooms":rooms})