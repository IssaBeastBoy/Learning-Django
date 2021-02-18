from django.shortcuts import render

# Create your views here.
def homepage(request):
    if (request.user.is_authenticated):   
       return render(request, "welcome.html", {})
    else:
         return render(request, "home.html", {})

'''

def FundingAv():

def Applications():

'''