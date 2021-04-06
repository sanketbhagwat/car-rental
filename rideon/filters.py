import django_filters
from django_filters import DateFilter
from .models import vehicles,bookings

class vehicleFilter(django_filters.FilterSet):
    # Category__in= django_filters.NumberFilter(field_name="Category", lookup_expr="in")
    # Category = django_filters.MultipleChoiceFilter(field_name="Category", lookup_expr="icontains")
    # category = django_filters.CharFilter(field_name='Category',lookup_expr="in"),
    # for i in Category:
        # print(i)
    # print(category)
    # Fuel_type=django_filters.ModelChoiceFilter(field_name='Fuel_type',queryset=vehicles.objects.all(),lookup_expr='in')
    start_date =django_filters.DateFilter(
         field_name='start_date',
         lookup_expr='lte') # use contains
    # print(start)
    
    End_date=DateFilter(field_name='End_date',lookup_expr='gte')

    class Meta:
        model=vehicles
        fields={'id','Vehicle_name','Fuel_type','Category','Gear_type','Company_name','Rent_cost','City'}
         
        # 

class BookingFilter(django_filters.FilterSet):
    class Meta:
        model=bookings
        fields=( 'carid','userid','phone','pickd','pickt','pickl','dropl','status')