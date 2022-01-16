from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contact.models import Contact
from django.core.mail  import send_mail
from django.contrib.auth.decorators import login_required
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['Password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print(user.email)
            send_mail(
                  'Welcome To CareZone',
                  'You have successfully login on carzone',
                  'hritickgi6445@gmail.com',
                  [user.email],
                  fail_silently=False,
            )
            messages.success(request,'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect("login")
    return render(request,'accounts/login.html')

def register(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
               messages.error(request,"User already exists!")
               return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                   messages.error(request,"Email already exists!")
                   return redirect('register')
                else:
                  user=User.objects.create_user(first_name=firstname,username=username,last_name=lastname,password=password,email=email)
                  auth.login(request,user)
                  send_mail(
                  'Welcome To CareZone',
                  'You have successfully registerd on carzone',
                  'hritickgi6445@gmail.com',
                   [email],
                   fail_silently=False,
                  )
                  messages.success(request,'Your are registerd successfully')
                  return redirect('dashboard')
                  user.save()
                  
                  
                  
                 
        else:
            messages.error(request,"Password dont match")
            return redirect("register")
    else:
       return render(request,'accounts/register.html')
def logout(request):
    print("logout")
    auth.logout(request)
    print("bjcjbvbsdbv")
    print("asbhfsvfsvjgshjfbshj")
    return redirect('home')

@login_required(login_url='login')
def dashboard(request):
    user_enquiry=Contact.objects.order_by('-create_date').filter(user_id=request.user.id)
    data={
        'inquiry':user_enquiry
    }
    
    return render(request,'accounts/dashboard.html',data)
