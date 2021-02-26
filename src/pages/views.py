from django.shortcuts import render
from profiles.models import Profile

# Create your views here.
def homepage(request):
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

def login(request):
    return render(request, "login.html", {})

'''

def FundingAv():

def Applications():

'''