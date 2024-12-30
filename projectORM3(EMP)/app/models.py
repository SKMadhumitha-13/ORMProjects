from django.db import models

# Create your models here.

class Department(models.Model):
    Dept_no= models.IntegerField(primary_key=True)
    Dept_name=models.CharField(max_length=100)
    Dept_loc= models.CharField(max_length=100)
    def __str__(self):
        return self.Dept_name

class Employee(models.Model):
    Emp_id=models.IntegerField(primary_key=True)
    Emp_name=models.CharField(max_length=100)
    Emp_job= models.CharField(max_length=100)
    Emp_sal=models.DecimalField(max_digits=10,decimal_places=2)
    Emp_comm=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    Dept_no=models.ForeignKey(Department,on_delete=models.CASCADE)
    Hiredate=models.DateField(auto_now=True)
    MGR=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return self.Emp_id