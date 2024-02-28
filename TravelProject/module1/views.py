import string
import random
from urllib import request

from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Register

# Create your views here.
def hello1(request):
    return HttpResponse("<centre>Welcome to Home page</centre>")

def newhomepage(request):
    return render(request, 'newhomepage.html')

def travelpackage(request):
    return render(request, 'travelpackage.html')

def car1(request):
    return render(request, 'car.html')

def print1(request):
    return render(request,'print_to_console.html')


def print_to_console(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'user input:{user_input}')
    a1 = {'user_input': user_input}
    return render(request, 'print_to_console.html',a1)


def randomcall(request):
    return render(request,'randomotpgenerator.html')


def randomlogic(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'user input:{user_input}')
        a2 = int(user_input)
        ran1 = ''.join(random.sample(string.digits, k=a2))
    a1 = {'ran1': ran1}
    return render(request, 'randomotpgenerator.html',a1)

def getdate1(request):
    return render(request,'get_date.html')

import datetime
from django.shortcuts import render
from .forms import *
def get_date(request):
    if request.method == 'POST':
        form = IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value = form.cleaned_data['integer_value']
            date_value = form.cleaned_data['date_value']
            updated_date = date_value + datetime.timedelta(days=integer_value)
            return render(request, 'get_date.html',{'updated_date':updated_date})
        else:
            form = IntegerDateForm()
        return render(request, 'get_date.html',{'form':form})


def register1(request):
    return render(request,'myregisterpage.html')


from django.shortcuts import render, redirect, HttpResponse
from .models import Register


def registerloginfunction(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phonenumber = request.POST.get('phonenumber')

        if Register.objects.filter(email=email).exists():
            return HttpResponse("Email already registered. Choose a different email.")

        Register.objects.create(name=name, email=email, password=password, phonenumber=phonenumber)
        return redirect('newhomepage')

    return render(request, 'myregisterpage.html')


import matplotlib.pyplot as plt
import numpy as np

def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart image
            img1={'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'piechart.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'piechart.html', {'form': form})

def weatherpagecall(request):
    return render(request, 'weatherpage.html')

def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = '54b5d0c61c6ff2ecd697067115cc3af6'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1= round(temperature - 273.15,2)
            return render(request, 'weatherappinput.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weatherappinput.html', {'error_message': error_message})


def contactmail(request):
    if request.method == 'POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        comment=request.POST['comment']
        tosend=comment + '______________________ This is just a test message'
        data=contactus(firstname=firstname, lastname=lastname, email=email, comment=comment, tosend=tosend)
        data=save()
        send_mail(
                'Thank you contacting uday travel tourism form',tosend,
        'uday26169@gmaiil.com',[email],
        fail_silently=False)

def send_emails(request):
    csv_file_path =
    with open(csv_file_path, 'r"C:\Users\uday2\Downloads\Book1.csv"') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            recipient_email = row['email']
            subject = 'Hello KLUian'  # Set your subject here
            message_body = 'Hey, Welcome to PFSD Class, Hope u have a great time with python'  # Set your email content here
            send_mail(
                subject,
                message_body,
                [recipient_email],
                fail_silently=False,
            )
            print(f'Sent email to {recipient_email}')
    return render(request, 'Emails_sent_successfully.html')


