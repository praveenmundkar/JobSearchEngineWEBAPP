from django.db.models import query_utils
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from JSE.models import States, Categories, Subcategories,CompanyDetails, Jobs


# # Create your views here.

def home(request):
    states = States.objects.all().values('state').distinct()
    context = {
        "states":states
    }
    return render(request, 'jse/home.html', context)

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
            messages.error(request, "passwords doesnt match")
            return redirect('/')
        if password1 != Password2:
            messages.error(request, "passwords doesnt match")
            return redirect('/')
        if username.isalnum() :
            pass
        else:
            messages.error(request, "The Username contains only letters and numbers")
            return redirect('/')
        # create user

        myuser = User.objects.create_user(username,email,password1)
        myuser.first_name = fname
        myuser.last_name = lname 
        myuser.save()
        messages.success(request, "Successfully Created JobSearch Engine Account ")

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
            messages.success(request, "Successfully Logged In")
            return redirect("/")
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('/')

def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect("/")


def categories(request):
    catq =(request.GET.keys())
    print(catq)
    for i in catq:
        catq=i
    print(catq)
    categories= Categories.objects.filter(state__icontains=catq)
    if catq == 'all':
        categories =Categories.objects.all()
    context = {
        'categories':categories
    }
    return render(request, 'jse/category.html', context)


def subcategories(request):
    subcatq = request.GET.keys()
    for i in subcatq:
        subcatq = i
    print(subcatq)
    subcategories = Subcategories.objects.filter(category__icontains=subcatq)
    if subcatq == 'all':
        subcategories = Subcategories.objects.all()
    context = {
        'subcategories':subcategories
    }
    return render(request, 'jse/subcategory.html', context)


def jobs(request):
    jobq = request.GET.keys()
    for i in jobq:
        jobq=i
    print(jobq)
    jobs = Jobs.objects.filter(subcategory__icontains=jobq)
    if jobq == 'al?l':
        jobs = Jobs.objects.all()
    context = {
        'jobs': jobs
    }
    return render(request, 'jse/job.html', context)

def company_details(request):
    cd = request.GET.keys()
    for i in cd:
        cd = i
    print(cd)
    company_details = CompanyDetails.objects.filter(name__icontains=cd)
    context = {
        'company_details':company_details
    }
    return render(request, 'jse/companydetail.html', context)



def searchstate(request):
    n=1
    query = request.GET['query']
    result1 = States.objects.filter(state__icontains=query).values('state').distinct()
    print(result1)
    try:
        result1[0]
    except:
        return render(request, 'jse/noresult.html')
    context = {
        'result1':result1, 'n':n
    }
    return render(request, 'jse/search.html',context)


def searchcat(request):
    n=2
    query = request.GET['query']
    result2 = Categories.objects.filter(category__icontains=query)
    try:
        result2[0]
    except:
        return render(request, 'jse/noresult.html')
    context = {
        'result2':result2,'n':n
    }
    return render(request, 'jse/search.html',context)


def searchsubcat(request):
    n=3
    query = request.GET['query']
    result3 = Subcategories.objects.filter(subcategory__icontains=query)
    try:
        result3[0]
    except:
        return render(request, 'jse/noresult.html')
    context = {
        'result3':result3,'n':n
    }
    return render(request, 'jse/search.html',context)

def searchjob(request):
    query = request.GET['query']
    result4 = Jobs.objects.filter(job_position__icontains=query)
    result5 = Jobs.objects.filter(location__icontains=query)
    result4 = result4 | result5
    print(result4)
    try:
        result4[0]
    except:
        return render(request, 'jse/noresult.html')
    context = {
        'result4':result4
    }
    return render(request, 'jse/search.html',context)