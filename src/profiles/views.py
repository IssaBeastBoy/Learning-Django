from django.shortcuts import render

# Create your views here.

from .form import LoginForm, New_user
from .models import Profile

def User_login(request):
    #users = Profile.objects.get(id=1) 
    form = LoginForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "form" : form,
        #"Object": users,
    }
    return render(request, "login.html", context)


def User_create(request):
    form = New_user(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "form" : form
    }
    return render(request, "NewUSER.html", context)