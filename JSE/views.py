from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return render(request, 'jse/home.html')

def handlesignup(request):
    if request.method == "POST":
        # Get the post parameters

        username =request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname= request.POST['lname']
        password1= request.POST['password1']
        Password2= request.POST['password2']

        # checks for signup
        if len(username)<4:
            return HttpResponse("username shoud be above 5 char")
        if password1 != Password2:
            return HttpResponse("confirm password is not same as password")
        if username.isalnum :
            return HttpResponse("letter ajhbsjh")
        # create user

        myuser = User.objects.create_user(username,email,password1)
        myuser.first_name = fname
        myuser.last_name = lname 
        myuser.save()

        return redirect("/")
    else:
        return HttpResponse("404 not found")

def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST["loginusername"]
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)

            return redirect("/")
        else:
            return HttpResponse("kjbjgv")

def handlelogout(request):
    logout(request)
    return redirect("/")
