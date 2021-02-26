from django.shortcuts import render

# Create your views here.

from .form import  New_user
from .models import Profile

def User_login(request):
    stop = 1
    Passwords = []
    Emails = []
    user_Name = ""
    while(stop <= Profile.objects.count()):
        users = Profile.objects.get(id=stop)
        Passwords.append(users.Password)
        Emails.append(users.Email)
        stop = stop +1
    context={
        "Emails": Emails,
        "Passwords": Passwords,
    }
    return render(request, "home.html", context)


def User_create(request):
    form = New_user(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "form" : form
    }
    return render(request, "NewUSER.html", context)

