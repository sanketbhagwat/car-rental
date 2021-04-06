from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from .models import vehicles,Add_Categories,Add_Company,bookings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date,datetime,timedelta
from django.core.paginator import Paginator
from .filters import vehicleFilter,BookingFilter
from django.views.generic.list import ListView
from rest_framework.generics import ListAPIView
from .serializer import VehicleSerializer
from django_filters.rest_framework import DjangoFilterBackend
import collections
from django.template import loader
from django import template


# @login_required(login_url="Accounts/login")
# def index(request):
    # 
    # context = {}
    # context['segment'] = 'index'
    # print("in for this")
    # html_template = loader.get_template( 'admin/index.html' )
    # return HttpResponse(html_template.render(context, request))
# 
# @login_required(login_url="Accounts/login")
# def pages(request):
    # context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    # try:
        # 
        # load_template      = request.path.split('/')
        # print(load_template)
        # load_template=load_template[1]+'/'+load_template[2]
        # context['segment'] = load_template
        # print(context['segment'])
        # 
        # html_template = loader.get_template( load_template )
        # print(html_template)
        # return HttpResponse(html_template.render(context, request))
        # 
    # except template.TemplateDoesNotExist:
# 
        # html_template = loader.get_template( 'admin/page-404.html' )
        # return HttpResponse(html_template.render(context, request))
# 
    # except:
    # 
        # html_template = loader.get_template( 'admin/page-500.html' )
        # return HttpResponse(html_template.render(context, request))
# 
# 

def validator():
    mydate=date.today()
    mindate=date.today()
    maxdate=(date.today()+timedelta(days=5))
    mindate2=(mindate + timedelta(days=1))
    maxdate2=(mydate+timedelta(days=60))
    mytime=datetime.now().time
    dict={'mydate':mydate,'mindate':mindate,'maxdate':maxdate,'mytime':mytime,'mindate2':mindate2,'maxdate2':maxdate2}
    return dict
# @login_required(login_url="/Accounts/login")
def homepage(request):
    vehicle=vehicles.objects.filter(status=True)
    man=Add_Categories.objects.all()
    man2=Add_Company.objects.all()
    print(man)
    print("you are ",request.session.get('customer_id'))
    print("your city:",request.session.get('city'))
    print(request.session.get('pickd'))
    for i in request.session.items():
        print(i)
    # mydate=date.today()
    # mindate=date.today()
    # maxdate=(date.today()+timedelta(days=5))
    # mindate2=(mindate + timedelta(days=1))
    # maxdate2=(mydate+timedelta(days=60))
    # mytime=datetime.now().time
    dict=validator()
    print(dict)
    context={'vehicles':vehicle, 'man':man,'man2':man2}
    context.update(dict)
    
    # return render(request,'homepage.html',{'vehicles':vehicle, 'man':man,'man2':man2,'context'=context})
    return render(request,'users/homepage.html',context=context)





# @login_required(login_url="/Accounts/login")
def listings(request):
    if request.method=='POST':
        # print(request.POST['selection'])
        # print("in post")
        category=request.POST.getlist('category[]')
        gear=request.POST.getlist('Geartype[]')
        print(gear)
        print(category)

        request.session['city']=request.POST.get('ctt')
        request.session['pickd']=request.POST.get('pdd')
        request.session['pickt']=request.POST.get('ptt')
        request.session['dropd']=request.POST.get('ddd')
        request.session['dropt']=request.POST.get('dtt')
        request.session['category']=request.POST.get('catid')
    
    category=request.GET.getlist('category[]')
    gear=request.POST.getlist('gear[]')
    print(gear)

    print(category)
    man=Add_Categories.objects.all()
    if request.GET.getlist('category'):
        request.session['category']=request.GET.get('category') 
    category_name=request.session.get('category')
    if category_name=="All":
        request.session['category_name']=category_name
        vehicle=vehicles.objects.filter(status=True).order_by('id')
        paginator=Paginator(vehicle,3)
        page_number=request.GET.get('page')
        page_obj=paginator.get_page(page_number)
        print(page_obj)
        dict=validator()
        context={'pro':page_obj,'manages':man}
        context.update(dict)
        return render(request,'users/listings.html',context=context)
    else:
        cat_name=Add_Categories.objects.filter(id=category_name).values('Add_New_Category')
        for i in cat_name:
            request.session['category_name']=i['Add_New_Category']
        category=vehicles.objects.filter(Category=category_name,status=True)
        paginator=Paginator(category,3)
        page_number=request.GET.get('page')
        page_obj=paginator.get_page(page_number)
        dict=validator()
        context={'pro':page_obj,'manages':man}
        context.update(dict)
        # return render(request,'listings.html',)
        return render(request,'users/listings.html',context=context)
    # man=ManageSite.objects.all()
    # category_name=request.GET.get('category')
    # print(category_name)
    # if category_name:
        # category=vehicles.objects.filter(Category=category_name)
        # return render(request,'listings.html',{'pro':category,'manages':man})
    # else:
        # pass
    # car_id=request.GET.get('ids')
    # man=ManageSite.objects.all()
    # vehicle=vehicles.objects.all()
    # if car_id:
        # car=vehicles.show_all_details(id)
        # return render(request,'booking.html',{'car':car})
    # else:
        # pass
    # return render(request,'booking.html',{'vehicles':vehicle})
    # return render(request,'listings.html',{'manages':man})

# def listingss(request):
    # vehicle=vehicles.objects.all()
    # filter=vehicleFilter(request.GET,queryset=vehicle)
    # return render(request,'listings.html',{'filter':filter})
def booking(request):
    if request.method=='POST':
        id=request.session.get('customer_id')
        if bookings.objects.filter(userid=id).exists():
            messages.info(request,'You Already have BOOKINGS')
            return redirect('/garage')
        else:
            user=User.objects.get(id=id)
            carid=request.session.get('car_id')
            car=vehicles.objects.get(id=carid)
            phone=request.POST['mob']
            pickd=request.POST['pd']
            pickt=request.POST['pt']
            pickl=request.POST['pl']
            dropd=request.POST['dd']
            dropt=request.POST['dt']
            dropl=request.POST['dl']
     
            booked=bookings.objects.create(carid=car,userid=user,phone=phone,pickd=pickd,pickt=pickt,pickl=pickl
                                ,dropd=dropd,dropt=dropt,dropl=dropl)
            vb=vehicles.objects.filter(id=carid).update(status=False)
            booked.save();
            return redirect('/garage')
    else:
        car_id=request.GET.get('ids')
        if car_id:
            car=vehicles.objects.filter(id=car_id)
            request.session['car_id']=car_id
            id=request.session.get('car_id')
            print("hey carid=",id)
            return render(request,'users/booking.html',{'car':car})
            

    
   
def bookingform(request):
    if request.method=='POST':
        
        id=request.session.get('customer_id')
        user=User.objects.get(id=id)
        carid=request.session.get('car_id')
        print(carid)
        car=vehicles.objects.get(id=carid)
        # print(userid,carid)
        phone=request.POST['mob']
        pickd=request.POST['pd']
        pickt=request.POST['pt']
        pickl=request.POST['pl']
        dropd=request.POST['dd']
        dropt=request.POST['dt']
        dropl=request.POST['dl']
        
        
        if pickd < str(date.today()):
            messages.error(request,'Date error')
            return redirect('bookingform')
        else:
            print("in the else")
            booked=bookings.objects.create(carid=car,userid=user,phone=phone,pickd=pickd,pickt=pickt,pickl=pickl
                                   ,dropd=dropd,dropt=dropt,dropl=dropl)
            vb=vehicles.objects.filter(id=carid).update(status=False)
            booked.save();
            return redirect('/garage')
    
    
    
    
    
    
    
    

def garage(request):
    # print("in garagaeeeee")
    # print(request.session.get('customer_id'))
    # id=request.session.get('customer_id')
    # print(request.session.get)
    # print("in")
    # print(bookings.objects.filter(userid=request.session.get('customer_id')))
    if bookings.objects.filter(userid=request.session.get('customer_id')):
            booking=bookings.objects.filter(userid=request.session.get('customer_id'))
        # if booking:
            car=bookings.objects.filter(userid=request.session.get('customer_id')).values('carid')
            for i in car:
                carid=i['carid']
            cardet=vehicles.objects.filter(id=carid)
            print(cardet)
            return render(request,'users/garage.html',{'bookings':booking,'cardet':cardet})
        # else:
            # return render(request,'garage.html')
    else:
        return render(request,'users/garage.html')
    # if request.session.get('customer_id'):
        # print(request.session.get('customer_id'))
        # booking=bookings.objects.all()
        # userid=request.session.get('customer_id')
        # filter=BookingFilter(request.session,queryset=bookings.objects.all())
        # print(filter.qs)
        # return render(request,'garage.html',{'filter':filter})


    
# class garage(View):
    # def get(self,request):
        # if bookings.objects.filter(userid=request.session.get('customer_id')):
        # if request.session['customer_id']:
            # print(request.session.get('customer_id'))
            # booking=bookings.object.all()
            # filter=BookingFilter(request.session,get('customer_id'))
# 
# 
# 
    
# Create your views here.
# 
# def booking(request):
    # pass

def update_booking(request):
    if request.method=='POST':
        dropd=request.POST['dd']
        dropt=request.POST['dt']
        dropl=request.POST['dl']
        userid=request.session.get('customer_id')
        bookings.objects.filter(userid=userid).update(dropd=dropd,dropt=dropt,dropl=dropl)
        return redirect('garage')
    else:
        userid=request.session.get('customer_id')
        booking=bookings.objects.filter(userid=userid)
        return render(request,'users/update.html',{'booking':booking})
    return render(request,'users/update.html')
def returncar(request):
    userid=request.session.get('customer_id')
    bookings.objects.filter(userid=userid).delete()
    return render(request,'users/garage.html')


def feedback(request):
    return render(request,'users/feedback.html')

def about(request):
    return render(request,'users/about.html')

def filterv(request):
    print("in filterv")



class ListingView(View):
    model=vehicles
    
    
    
    
    # queryset = vehicles.objects.all()
    # filter_backends = [DjangoFilterBackend]
    # filterset_class = vehicleFilter
    # serializer_class =VehicleSerializer
   
    def get(self,request):
        # categories=Add_Categories.objects.all()
        # companies=Add_Company.objects.all()
        # vehicle=vehicles.objects.all()  #filter(status=True)
        # print(vehicle)
        
        # vehicle=vehicles.objects.all().filter(status=True,Gear_type__in=request.GET.getlist('Geartype'),
                                                # Fuel_type__in=request.GET.getlist('fueltype'),
                                                # Category__in=request.GET.getlist('catgeory'))
        request.session['City']=request.GET.get('City')
        request.session['start_date']=request.GET.get('start_date')
        print( request.session.get('start_date'))
        request.session['start_time']=request.GET.get('start_time')
        request.session['End_date']=request.GET.get('End_date')
        request.session['End_time']=request.GET.get('End_time')
        vehicle=vehicles.objects.all()
        categories=Add_Categories.objects.all()
        companies=Add_Company.objects.all()
        category=request.GET.getlist('Category')
        print("in cat",category)
        print(request.GET.getlist('Category'))
        filter=vehicleFilter(request.GET,queryset=vehicle)
        # queryset=vehicle
        # serializer_class = VehicleSerializer
        # pagination_class = GoodsPagination
        # filter_backends = (DjangoFilterBackend,)
        # filter_class = vehicleFilter
        # print(filter_class)
       
        print(filter.qs)
        # ----------------pagination-------------------------                                         
        paginator=Paginator(filter.qs,4)
        print(paginator)
        page_number=request.GET.get('page')
        print(page_number)
        page_obj=paginator.get_page(page_number)
        context={'categories':categories,'companies':companies,'pro':page_obj}
        dict=validator()
        context.update(dict)
        return render(request,'users/listingss.html',context=context)
        # return render(request,'listings.html',context=context)
    def post(self,request):
        # category=request.POST.getlist('category[]')
        # gear=request.POST.getlist('Geartype[]')
        # print(gear)
        # print(category)
        request.session['City']=request.POST.get('ctt')
        request.session['pickd']=request.POST.get('pdd')
        request.session['pickt']=request.POST.get('ptt')
        request.session['dropd']=request.POST.get('ddd')
        request.session['dropt']=request.POST.get('dtt')
        request.session['Category']=request.POST.get('catid')

        if request.session.get('Category')=="All":
            request.session['Category']="All"
            request.session['category_name']="All"
            paginator=Paginator(self.vehicle,4)
            print(paginator)
            page_number=request.GET.get('page')
            print(page_number)
            page_obj=paginator.get_page(page_number)
            context={'categories':self.categories,'companies':self.companies,'pro':page_obj}
            return render(request,'users/listingss.html',context=context)
        else:
            cat_name=Add_Categories.objects.filter(id=request.session.get('Category')).values('Add_New_Category')
            request.session['category_name']=cat_name
            values=collections.defaultdict(list)
            values['Category'].append(request.session['Category'])
            filter=vehicleFilter(values,queryset=self.vehicle)
            print(filter.qs)
            print("in post")
            request.session['Category']="cat_name"
            paginator=Paginator(filter.qs,4)
            print(paginator)
            page_number=request.GET.get('page')
            page_obj=paginator.get_page(page_number)
            context={'categories':self.categories,'companies':self.companies,'pro':page_obj}
            return render(request,'users/listingss.html',context=context)

            

