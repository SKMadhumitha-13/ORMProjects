from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.

def insert_topic(request):
    tn=input('Enter Topic Name:')
    TOD= Topic.objects.get_or_create(topic_name=tn)
    if TOD[1]:
        return HttpResponse('New Topic is Created!!!')
    else:
        return HttpResponse('Given Topic is already Present!!!')
    
def insert_Webpage(request):
    tn=input('Enter the topic name:')
    nm=input('Enter the name:')
    url=input('Enter the url:')
    email=input('Enter the email:')
    LTO= Topic.objects.filter(topic_name=tn)
    if LTO:
        WTOD =Webpage.objects.get_or_create(topic_name=LTO[0],name=nm,url=url,email=email)
        if WTOD[1]:
            return HttpResponse('Web is created!!')
        else:
            return HttpResponse('Web is Present!!!')
        
    else:
        return HttpResponse('Given Topic is not Present!!')
    
def insert_AccessRecord(request):
    pk=int(input('Enter pk of Webpage:'))
    name=input('Enter the name:')
    author=input('Enter the author:')
    date=input('Enter the date:')
    LWO=Webpage.objects.filter(pk=pk)
    if LWO:
        WO=LWO[0]
        ATOD=AccessRecord.objects.get_or_create(name=WO,author=author,date=date)

        if ATOD[1]:
            return HttpResponse('New Access is created!!')
        else:
            return HttpResponse('With given details,Access is already Present!!')
    else:
        return HttpResponse('Given Parent Webpage Table Data is not Present in Database!!!')
    
def display_topics(request):
    LTO= Topic.objects.all()
    d= {'LTO':LTO}
    return render(request,'display_topics.html',d)

def display_webpage(request):
    WTO=Webpage.objects.all()
    d={'WTO':WTO}
    return render(request,'display_webpage.html',d)

def display_accessrecord(request):
    ATO=AccessRecord.objects.all()
    d={'ATO':ATO}
    return render(request,'display_accessrecord.html',d)