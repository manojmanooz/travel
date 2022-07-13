from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):

    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"INVALID USER")
            return redirect('login')
    return render(request,'login.html')



def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        first=request.POST['firstname']
        last=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exists')


            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')

            else:

                user = User.objects.create_user(username=username, first_name=first, last_name=last, email=email,
                                        password=password)
                user.save();
                messages.info(request,'REGISTERED SUCCESFULLY')
                return redirect('login')
        else:
            messages.info(request,'REGISTRATION FAILED')
            return redirect('register')
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

