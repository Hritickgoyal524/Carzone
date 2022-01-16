from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact
from django.core.mail  import send_mail
from django.contrib.auth.models import User
def inquiry(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        car_id=request.POST['car_id']
        car_title=request.POST['car_title']
        city=request.POST['city']
        customer_need=request.POST['customer_need']
        state=request.POST['state']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        user_id=request.POST['user_id']
        if request.user.is_authenticated:
            user_id=request.user.id
            has_contacted=Contact.objects.all().filter(car_id=car_id,user_id=user_id)
            if has_contacted:
               messages.error(request,"Your have already made a request, we will get back to you shortly")
               return redirect("/cars/"+car_id)
        contact=Contact(first_name=first_name,last_name=last_name,car_id=car_id,car_title=car_title,city=city,customer_need=customer_need,state=state,email=email,phone=phone,message=message,user_id=user_id)
        contact.save()
        admin_info =User.objects.get(is_superuser=True)
        admin_email=admin_info.email
        send_mail(
            'New Car Inquiry',
            'You have a new inquiry for the car' + car_title + '.Please login to your admin panel for more info.',
            'hritickgi6445@gmail.com',
            [admin_email],
            fail_silently=False,
        )
        messages.success(request,"Your request has been submitted, we will get back to you shortly")
        return redirect("/cars/"+car_id)