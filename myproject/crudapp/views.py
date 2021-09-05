from crudapp.models import students
from django.shortcuts import render,redirect
from django.http import HttpResponse 
from.models import students

# Create your views here.

def demo(request):
    if request.method == "POST":
        sname = request.POST.get('sname')
        sroll = request.POST.get('sroll')
        semail = request.POST.get('semail')
        smobail = request.POST.get('smobail')
        sbranch = request.POST.get('sbranch')
        students.objects.create(sname=sname,sroll=sroll,semail=semail,smobail=smobail,sbranch=sbranch)
        return HttpResponse("Recorde insted into table")  
    return render(request, 'myapp/demo.html')


def show(request):
    data = students.objects.all()
    return render(request, 'myapp/show.html',{'data':data})

def update(request,id):
    rec = students.objects.get(id=id)
    if request.method == "POST":
        rec.sname = request.POST.get('sname')
        rec.sroll = request.POST.get('sroll')
        rec.semail = request.POST.get('semail')
        rec.smobail = request.POST.get('smobail')
        rec.sbranch = request.POST.get('sbranch')
        rec.save()
        #return HttpResponse("Update Succesfully your details")
        return redirect('show')
    return render(request, 'myapp/update.html',{'rec':rec})  


def delete(request,id):
    del_rec = students.objects.get(id=id)
    if request.method == "POST":
        del_rec.delete()
        del_rec.save()
        return redirect('show')
    return render(request, 'myapp/delete.html',{'del_rec':del_rec})          