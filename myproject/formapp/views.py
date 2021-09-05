from django.shortcuts import render,redirect
from django.http import HttpResponse 
from formapp.models import Register
from formapp.form import Reg

# Create your views here

def register(request):
    if request.method == 'POST':
        formdata=Reg(request.POST)
        if formdata.is_valid():
            formdata.save()
            return redirect('details')
    formdata = Reg()
    return render(request,'myapp/register.html',{'data': formdata})

def details(request):
    data = Register.objects.all()
    return render(request,'myapp/details.html',{'data': data})

def replace(request,id):
    a= Register.objects.get(id=id)
    if request.method =="POST":
        u=Reg(request.POST,instance=a)
        if u.is_valid():
            u.save()
            return redirect('details')
    u=Reg(instance=a)
    return render(request,'myapp/replace.html',{'u':u})

def dell(request,id):
    d= Register.objects.get(id=id)
    if request.method =="POST":
        d.delete()
        return redirect('details')
    return render(request,'myapp/dell.html',{'d':d})  