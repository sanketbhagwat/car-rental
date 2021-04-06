from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
import datetime

dates=datetime.date.today()
dates+=datetime.timedelta(days=30)
FuelTypes=(
    ('petrol','petrol'),('diesel','diesel'),('electric','Electric')
)

GearType=(('manual','manual'),('automatic','automatic'))
category=(('hatchback','hatchback'),('sedan','sedan'),('suv','suv'),('bike','motorcycle'),('tourist','tourist'))

class Add_Categories(models.Model):
    Add_New_Category=models.CharField(max_length=20)
    Category_vehicle_img=models.ImageField(upload_to='images',default='')

    def __str__(self):
        return self.Add_New_Category

class Add_Company(models.Model):
    Add_New_Company=models.CharField(max_length=20)
    Add_Company_Logo=models.ImageField(upload_to='images',default='')

    def __str__(self):
        return self.Add_New_Company

# class Add_Fuel_type(models.Model):
    # Add_New_type=models.CharField(max_length=20)
# 

class location(models.Model):
    street=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    country=models.CharField(max_length=20)

    def __str__(self):
        return self.city
    
    
    
    

# cat=Manage_site.objects.all()
class vehicles(models.Model):
    # Category=models.CharField(max_length=20,choices=category,default='hatchback')
    Category=models.ForeignKey(Add_Categories,on_delete=models.CASCADE)
    Company_name=models.ForeignKey(Add_Company,on_delete=models.CASCADE)
    Vehicle_name=models.CharField(max_length=50)
    Seat_capacity=models.IntegerField(default=1)
    Fuel_type=models.CharField(max_length=20,choices=FuelTypes,default='petrol')
    Gear_type=models.CharField(max_length=20,choices=GearType,default='manual')
    Year_of_mfg=models.IntegerField(default=2000)
    Rent_cost=models.IntegerField()
    City=models.ForeignKey(location,on_delete=models.CASCADE)
    Front_img=models.ImageField(upload_to='images')
    Side_img=models.ImageField(upload_to='images')
    Rear_img=models.ImageField(upload_to='images')
    start_date=models.DateField(default=datetime.date.today)
    End_date=models.DateField(default=dates)
    status=models.BooleanField(default=True)
    
    def __str__(self):
        return self.Vehicle_name
    

class bookings(models.Model):
    carid=models.ForeignKey(vehicles,on_delete=models.CASCADE)
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=10)
    pickd=models.DateField()
    pickt=models.TimeField()
    pickl=models.CharField(max_length=10)
    dropd=models.DateField()
    dropt=models.TimeField()
    dropl=models.CharField(max_length=10)
    status=models.BooleanField(default=False,verbose_name='Accept')
    







