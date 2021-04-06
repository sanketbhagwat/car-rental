from django.contrib import admin
from django.contrib.auth.models import Group
from .models import vehicles,Add_Categories,Add_Company,bookings,location

admin.site.site_header='Ride on>>>'


class vehiclesadm(admin.ModelAdmin):
    list_display=('id','Category','Company_name','Vehicle_name','Seat_capacity','City','Gear_type','Front_img','Side_img','Rear_img','status')
    list_filter=('Category','Company_name','status')

class bookingsadm(admin.ModelAdmin):
    list_display=('id','carid','userid','phone','pickd','pickt','pickl','dropd','dropt','dropl','status')

class locationadm(admin.ModelAdmin):
    list_display=('id','street','city','state','country')



admin.site.unregister(Group)
admin.site.register(vehicles,vehiclesadm)
admin.site.register(bookings,bookingsadm)
admin.site.register(Add_Categories)
admin.site.register(Add_Company)
admin.site.register(location,locationadm)
# Register your models here.