from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.

def insert_Course(request):
    cid=int(input('Enter the Course ID:'))
    c_name=input('Enter the Course name:')
    t_name=input('Enter the trainer name:')
    CTO=Course.objects.get_or_create(CID=cid,Cname=c_name,Trainername=t_name)

    if CTO[1]:
        return HttpResponse('Course is Created!!')
    else:
        return HttpResponse('Course is not Created!!')
    
def insert_Student(request):
    sid=int(input('Enter the Student ID:'))
    s_name=input('Enter the Student Name:')
    s_marks=int(input('Enter the marks of the student:'))
    cid=int(input('Enter the Course ID:'))
    cidobj=Course.objects.get(CID=cid)

    STO=Student.objects.get_or_create(SID=sid,Sname=s_name,Marks=s_marks,CID=cidobj)
    if STO[0]:
        return HttpResponse('Student details is added!!')
    else:
        return HttpResponse('With the given details, student is already available!!')

def display_course(request):
    CTO=Course.objects.all()
    d={'CTO':CTO}
    return render(request,'display_course.html',d)

def display_student(request):
    STO=Student.objects.all()
    d={'STO':STO}
    return render(request,'display_student.html',d)    