from django.shortcuts import render,redirect
from .models import Team
from cars.models import Car
from django.contrib import messages
from django.core.mail  import send_mail
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    team=Team.objects.all()
    featured_car=Car.objects.order_by('-created_date').filter(is_featured=True)
    all_car=Car.objects.order_by('-created_date')#decresing order (- sign for decreasing)
    # search_field=Car.objects.values("model",'body_style','city','year')
    model=Car.objects.values_list('model',flat=True).distinct()
    city=Car.objects.values_list('city',flat=True).distinct()
    year=Car.objects.values_list('year',flat=True).distinct()
    body_style=Car.objects.values_list('body_style',flat=True).distinct()
    context={
        "teams":team,
        "featured_car":featured_car,
        "All_car":all_car,
        "city":city,
        "year":year,
        "body_style":body_style,
        "model":model
    }
    return render(request,'pages/home.html',context)
def about(request):
      team=Team.objects.all()
      context={
        "teams":team
      }
      return render(request,'pages/about.html',context)
def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        phone=request.POST['phone']
        message=request.POST['message']
        email_sub="You have a new message from Carzone regarding"+ subject
        message_body='Name:'+ name + 'Email:' + email + 'Phone:' + phone + "Message:" + message
        messages.success(request,"Thank you for contacting us. We will get back to you shortly.")

        admin_info= User.objects.get(is_superuser=True)
        print("admin_info")
        print(admin_info)        
        admin_email=admin_info.email
        print("admin_email")
        print(admin_email)    
        send_mail(
            email_sub,
            message_body,
            'hritickgi6445@gmail.com',
            [admin_email],
            fail_silently=False,
        )
        return redirect('contact') 
    return render(request,'pages/contact.html')
def services(request):
    return render(request,'pages/services.html')