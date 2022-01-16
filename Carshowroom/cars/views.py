from django.shortcuts import render,get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
def car(request):
    cars=Car.objects.order_by('-created_date')
    paginator=Paginator(cars,2)
    page=request.GET.get('page')
    paged_car=paginator.get_page(page)
    model=Car.objects.values_list('model',flat=True).distinct()
    city=Car.objects.values_list('city',flat=True).distinct()
    year=Car.objects.values_list('year',flat=True).distinct()
    body_style=Car.objects.values_list('body_style',flat=True).distinct()

    data={
        "Cars":paged_car,
        "model":model,
        "city":city,
        "year":year,
        "body_style":body_style

    }
    return render(request,"cars/cars.html",data)

def car_details(request,id):
    single_car=get_object_or_404(Car,pk=id)
    data={
        "single_car":single_car
    }
    return render(request,'cars/cars_detail.html',data)

def search(request):
    cars=Car.objects.order_by('-created_date')
    model_search=Car.objects.values_list('model',flat=True).distinct()
    city_search=Car.objects.values_list('city',flat=True).distinct()
    year_search=Car.objects.values_list('year',flat=True).distinct()
    body_style=Car.objects.values_list('body_style',flat=True).distinct()
    transmission_search=Car.objects.values_list('transmission',flat=True).distinct()
    if 'keyword' in request.GET:
        keyword=request.GET['keyword']
        if keyword:
            cars=cars.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model=request.GET['model']
        if model:
            cars=cars.filter(model__iexact=model)
            print("car",cars)
    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            cars=cars.filter(city__iexact=city)
            print("car",cars)
    if 'year' in request.GET:
        year=request.GET['year']
        if year:
            cars=cars.filter(year__iexact=year)
            print("car",cars)
    if 'body' in request.GET:
        body=request.GET['body']
        if body:
            cars=cars.filter(body_style__iexact=body)
            print("car",cars)
    if 'min_price' in request.GET:
        min_price=request.GET['min_price']
        max_price=request.GET['max_price']
        if max_price:
            cars=cars.filter(price__gte=min_price,price__lte=max_price)
            print("car",cars)
    data={
        "Cars":cars,
        "model":model_search,
        "city":city_search,
        "year":year_search,
        "body_style":body_style,
        "transmission":transmission_search
    }
    return render(request,'cars/search.html',data)

