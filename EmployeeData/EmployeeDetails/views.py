from django.shortcuts import render

from django.http import HttpResponse
import datetime
from .models import EmployeeData
def display(request):
    now = datetime.datetime.now()
    html="<html><h1>welcome to django application</h1></html>"
    return HttpResponse(html)

def get_employee_data(request):
    out=EmployeeData.objects.all()
    return render(request,'employee_data.html',{'data': out})