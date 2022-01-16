from django.contrib import admin

from django.urls import path
from . import views
urlpatterns = [
    path('',views.car,name="cars"),
    path('<int:id>',views.car_details,name="car_details"),
    path("search",views.search,name="search")
   
]
