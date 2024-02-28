from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('hello1/', hello1, name='hello1'),
    path('', newhomepage, name='newhomepage'),
    path('travelpackage/', travelpackage, name='travelpackage'),
    path('print_to_console/', print_to_console, name='print_to_console'),
    path('print1/', print1, name='print1'),
    path('randomlogic/', randomlogic, name='randomlogic'),
    path('randomcall/', randomcall, name='randomcall'),
    path('getdate1/', getdate1, name='getdate1'),
    path('get_date/', get_date, name='get_date'),
    path('register1/',register1,name='register1'),
    path('registerloginfunction/',registerloginfunction,name='registerloginfunction'),
    path('pie_chart/', pie_chart, name='pie_chart'),
    path('car1/', car1, name='car1'),
    path('weatherlogic/',weatherlogic,name='weatherlogic'),
    path('weatherpagecall/',weatherpagecall,name='weatherpagecall')
    path('mailapp/', include('mailapp.urls')),
    path('reviewsapp',include('reviewsapp.urls')),


]