from django.shortcuts import render
from testapp.models import Employee
from testapp.forms import EmployeeForm
from django.http import HttpResponseRedirect

# Create your views here.
def retrieve_view(request):
    employees=Employee.objects.all()
    return render(request,'testapp/index.html',{'employees':employees})

def create_view(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    return render(request,'testapp/create.html',{'form':form})

def delete_view(request,id):
    if request.objects=='POST':
        employee=Employee.objects.grt(id=id)
        employee.delete()
    return HttpResponseRedirect('/')


def update_view(request,id):
    employee=Employee.objects.get(id=id)
    if request.method=='POST':
        form=EmployeeForm(request.post,instance=employee)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    return render(request,'testapp/update.html',{'employee':employee})