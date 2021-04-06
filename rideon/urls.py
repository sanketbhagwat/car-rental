from django.urls import path,include,re_path
from . import views
from .models import vehicles
urlpatterns=[
    path('',views.homepage,name='Ride on'),
    re_path('listings/',views.ListingView.as_view(),name='listing'),
    # re_path('request.get_full_path/',views.ListingView.as_view(),name='listing'),
    # re_path(r"^listings/",views.listings,name='listings'),
    path('booking/',views.booking,name='bookings'),
    # path('booking/booking',views.booking,name='bookings'),
    # path('/filterv',views.filterv,name='filterv'),
    # path('garage',views.garage.as_view(),name='garage'),
    path('garage',views.garage,name='garage'),
    path('return',views.returncar,name='Re-turn'),
    path('update-booking',views.update_booking,name='update_booking'),
    path('about',views.about,name='about'),
    path('feedbacks',views.feedback,name='feedback'),
    path('bookingform',views.bookingform,name='bookingform'),
    path('bookingform/booking',views.bookingform,name='bookings'),
    #path('', views.index, name='home'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),
    
]