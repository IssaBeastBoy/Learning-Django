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
    user_Password = request.POST.get("Password")
    user_Email = request.POST.get("Email")
    if user_Email is not None:
        bool_countEmail = 0
        bool_countPassword = 0
        count = 0        
        while count < len(Emails):
            if user_Email == Emails[count]:
                bool_countEmail = bool_countEmail + 1
                users = Profile.objects.get(id=count+1)
                user_Name = str(users.Name) + " " + str(users.Surname)
            if user_Password == Passwords[count]:
                bool_countPassword = bool_countPassword + 1
            count = count + 1
            if count == len(Emails):
                if bool_countEmail != 1 and bool_countPassword != 1:
                    return render(request, "login wrgBoth.html", {})
                elif bool_countEmail == 1 and bool_countPassword != 1:
                    return render(request, "login wrgPass.html", {})
                elif bool_countEmail != 1 and bool_countPassword == 1:
                    return render(request, "login wrgEmail.html", {})
                else:
                    context ={
                        "UserName": user_Name
                    }                    
                    return render(request, "welcome.html",context)
           
    return render(request, "login.html", {})


def User_create(request):
    form = New_user(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "form" : form
    }
    return render(request, "NewUSER.html", context)

