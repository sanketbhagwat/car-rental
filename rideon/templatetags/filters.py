from django import template
from django.utils import timezone
from datetime import date
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from rideon.models import vehicles,Add_Categories,Add_Company,bookings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date,datetime,timedelta

register=template.Library()

@register.filter(name='sessions')
def sessions(val):
#      city=request.session.get('city')
#      pickd=request.session.get('pickd')
#      pickt=request.session.get('pickt')
#      dropd=request.session.get('dropd')
#      dropt=request.session.get('dropt')
#      cat=request.session.get('category')
     return False
@register.filter(name='check')
def check(val):
     print('in chackkkkkkkkkkkkk')
     