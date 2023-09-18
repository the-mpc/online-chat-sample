from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path("login/",views.signin),
    path("signup/", views.signup),
    path("signout/", views.signout),
]