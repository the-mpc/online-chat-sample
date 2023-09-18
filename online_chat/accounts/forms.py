from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
class SignIn(AuthenticationForm):
    username = forms.CharField(max_length=200,label="",widget=forms.TextInput(attrs={"placeholder":"your username"}))
    password = forms.CharField(max_length=200,label="",widget=forms.PasswordInput(attrs={"placeholder":"your password"}))
    captcha = ReCaptchaField(label="",widget=ReCaptchaV2Checkbox)
    class Meta():
        model = User
        fields = ("username","password","captcha")
class SignUp(UserCreationForm):
    captcha = ReCaptchaField(label="",widget=ReCaptchaV2Checkbox)
    username = forms.CharField(max_length=200,label="",widget=forms.TextInput(attrs={"placeholder":"your username"}))
    password1 = forms.CharField(max_length=200,label="",widget=forms.PasswordInput(attrs={"placeholder":"your password"}))
    password2 = forms.CharField(max_length=200,label="",widget=forms.PasswordInput(attrs={"placeholder":"re type your password"}))
    email = forms.EmailField(required=False,max_length=200,label="",widget=forms.EmailInput(attrs={"placeholder":"your email (optional)"}))
    first_name = forms.CharField(required=False,max_length=200,label="",widget=forms.EmailInput(attrs={"placeholder":"your name (optional)"}))
    last_name = forms.CharField(required=False,max_length=200,label="",widget=forms.EmailInput(attrs={"placeholder":"your family (optional)"}))
    class Meta():
        model = User
        fields = ("username","password1","password2","email","first_name","last_name","captcha")