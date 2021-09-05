from django.shortcuts import render

# Create your views here.

def table(request):
    return render(request, 'myapp/table.html')

def table2(request):
    return render(request, 'myapp/table2.html')

def task(request,num):
    data=[]
    for i in range(1,11):
        td = str(num)+"*"+str(i)+"="+str(num*i)
        data.append=(td)
    return render(request, 'myapp/task.html',{'info':data}) 

def bootonline(request):
    return render(request, 'myapp/bootonline.html')

def bootoffline(request):
    return render(request, 'myapp/bootoffline.html')    
