from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.

def insert_Department(request):
    dept_no=int(input('Enter the Deptno:'))
    dept_name=input('Enter the Dept Name:')
    dept_loc=input('Enter the Location:')
    DTO=Department.objects.get_or_create(Dept_no=dept_no,Dept_name=dept_name,Dept_loc=dept_loc)
    if DTO[1]:
        return HttpResponse('Department is created!!')
    else:
        return HttpResponse('Department is not created!!!')

def insert_Employee(request):
    Empno=int(input('Enter the Emp no:'))
    Ename=input('Enter the emp Name:')
    job=input('Enter the Job:')
    Sal=int(input('Enter the sal of the employee:'))
    hiredate=input('Enter the date of Hiring:')
    comm=input('Enter the Commission:')
    if comm:
        comm= int(comm)
    else:
        comm=None

    mgr=input('Enter the MGR no. of the employee:')
    if mgr:
        mgr=int(mgr)
        mgro=Employee.objects.filter(Empno=mgr)
        if mgro:
           mg=mgro[0]
        else:
            mg=None
    else:
        mg= None

    dept_no=int(input('Enter the deptno:'))
    deptobj=Department.objects.get(Dept_no=dept_no)
    
    ETO=Employee.objects.get_or_create(Emp_id=Empno,Emp_name=Ename,Emp_sal=Sal,Emp_job=job,
    Hiredate=hiredate,Emp_comm=comm,MGR=mg,Dept_no=deptobj)
    if ETO[0]:
        return HttpResponse('New employee is added!!')
    else:
        return HttpResponse('With the given details, the employee is already Present!!! ')
    
def display_department(request):
    DTO=Department.objects.all()
    d={'DTO':DTO}
    return render(request,'display_department.html',d)

def display_employee(request):
    ETO=Employee.objects.all()
    d={'ETO':ETO}
    return render(request,'display_employee.html',d)