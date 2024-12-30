from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.

def insert_Country(request):
    C_no=int(input('Enter the Country no:'))
    C_name=input('Enter the Country Name:')
    CTO=Country.objects.get_or_create(Country_no=C_no,Country_name=C_name)
    if CTO[1]:
        return HttpResponse('Country is Created!!!')
    else:
        return HttpResponse('Country is not Created!!')
    
def insert_capital(request):
    ca_no=int(input('Enter the Capital No.'))
    ca_name=input('Enter the Capital Name:')
    C_name=input('Enter the Country name:')
    C_nameobj=Country.objects.get(Country_name=C_name)
    CATO=Capital.objects.get_or_create(Capital_no=ca_no,Capital_name=ca_name,Country_name=C_nameobj)
    if CATO[0]:
        return HttpResponse('Capital is created!!!')
    else:
        return HttpResponse('With the given details, the Country\'s capital is exisiting!! ')
    
def display_country(request):
    CTO=Country.objects.all()
    d={'CTO':CTO}
    return render(request,'display_country.html',d)

def display_capital(request):
    CATO=Capital.objects.all()
    d={'CATO':CATO}
    return render(request,'display_capital.html',d)    