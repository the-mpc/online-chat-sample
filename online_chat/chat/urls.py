from django.urls import path
from . import views

app_name = "chat"
urlpatterns = [
    path("checkview", views.checkview, name="checkview"),
    path("send/<roomcode>",views.send,name="send"),
    path("<rc>", views.room, name="room"),
]