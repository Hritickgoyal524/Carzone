from django.contrib import admin
from . models import Team
from django.utils.html import format_html
class Teamadmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40px" style="border-radius:50px;">'.format(object.photo.url))
    thumbnail.short_description="photo"
    list_display=('id','thumbnail','firstname','designation','created_date')
    list_display_links=('id','thumbnail','firstname',)
    list_filter=('designation',) #side filter
    search_fields=("firstname","lastname","designation")

admin.site.register(Team,Teamadmin)
