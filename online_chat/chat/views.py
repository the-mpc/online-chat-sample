from django.shortcuts import render,redirect
from . import models as db
def room(request,rc):
    rm = db.Room.objects.filter(room_code=rc)
    messages = db.Message.objects.filter(code=rc)
    return render(request,"room.html",{"room":rm,"messages":messages})
def checkview(request):
    room_code = request.POST.get("room_code")
    if db.Room.objects.filter(room_code=room_code).exists():
        return redirect("/chat/"+room_code)
    else:
        new_room = db.Room.objects.create(room_code=room_code,created_by=request.user)
        new_room.save()
        return redirect("/chat/"+room_code)
def send(request,roomcode):
    val = request.POST.get("send")
    room = db.Room
    room = room.objects.filter(room_code=roomcode)
    new_message = db.Message.objects.create(value=val,user=request.user,rc=room[0],code=roomcode)
    new_message.save()
    return redirect("/chat/"+roomcode)