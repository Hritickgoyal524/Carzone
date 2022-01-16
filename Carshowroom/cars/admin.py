from django.contrib import admin
from .models import Car
from django.utils.html import format_html
class Caradmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40px" style="border-radius:50px;">'.format(object.car_photo.url))
    thumbnail.short_description="Car Image"
    list_display=('id','thumbnail','car_title','city','color','model','year','body_style','fuel_type','is_featured')
    list_display_links=('id','thumbnail','car_title',)
    list_filter=('city','fuel_type','model','body_style') #side filter
    search_fields=("car_title","model","city","body_style","fuel_type")
    list_editable=('is_featured',)

admin.site.register(Car,Caradmin)
