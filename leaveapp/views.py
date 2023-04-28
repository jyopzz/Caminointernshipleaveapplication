
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Leaveapply, Leavedetails,Admindata




# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')   



def logged(request):
    if request.method == 'GET':
        username = request.GET['username']
        password = request.GET['password']
        if username == 'admin' and password == 'admin':
            return redirect('admindash')
        elif username == 'emp' and password == 'emp':
            return redirect('empdash')
        else:
            return HttpResponse('incorrect username or password')

def admindash(request):
    return render(request,'admindash.html')  


def addadmin(request):
    return render(request,'addadmin.html')  
    
def empdetails(request):
    return render(request,'employeedetails.html')
    
def leavedetails(request):
    Leavedetailsobj=Leavedetails.objects.all()
    return render(request,'leavedetails.html',{'all':Leavedetailsobj})  

def addemployee(request):
    return render(request,'addemployee.html')   

def empdash(request):
    return render(request,'employeedash.html') 

def leaveapply(request):
    return render(request,'leave-apply.html') 

def leavestatus(request):
    userid = request.user.id
    x=Leavedetails.objects.filter(userid=userid)
    return render(request,'leavestatus.html', {'all': x})

#load the leave details to the leaveapprove page
def leaveapprove1(request,i):     
    e=Leavedetails.objects.filter(id=i)
    return render(request,'leaveapprove.html',{'all': e})

def leavereject1(request,i):     
    e=Leavedetails.objects.filter(id=i)
    return render(request,'leavereject.html',{'all': e})
    




#redirecting admin functions start

def logout(request):
    return redirect('index')  

def admindash1(request):
    return redirect('admindash')    

def empdetails1(request):
    return redirect('empdetails')

def leavedetails1(request):
    return redirect('leavedetails')

#redirecting admin functions end

#redirecting  emp functions start
def empdash1(request):
    return redirect('empdash')

def leavestatus1(request):
    return redirect('leavestatus')    

def leaveapply1(request):
    return redirect('leaveapply') 
#redirecting  emp functions end

def empleave(request):
    if request.method=='POST':
        userid = request.user.id
        name=request.POST['name']
        empid=request.POST['empid']
        startingdate=request.POST['startingdate']
        endingdate=request.POST['endingdate']
        reason=request.POST['reason']
        print(userid,name,empid,startingdate,endingdate,reason)
        Leaveapplyobj=Leaveapply()
        Leaveapplyobj.name=name
        Leaveapplyobj.empid=empid
        Leaveapplyobj.startingdate=startingdate
        Leaveapplyobj.endingdate=endingdate
        Leaveapplyobj.reason=reason
        Leaveapplyobj.save()

        #database Leavedetails
        Leavedetails(userid=userid,name=name,empid=empid,startingdate=startingdate,endingdate=endingdate,reason=reason,status='pending').save()

        return redirect('leaveapply')

def leaveapprove(request,i):
    if request.method=='POST':
            x=Leavedetails.objects.get(id=i)
            x.status='Approved'
            x.save()
            x=Leavedetails.objects.all()
            return redirect('leavedetails1')
            #return render(request,'leavedetails.html', {'all':x})
    else:
        x = Leavedetails.objects.all()
        return render(request, 'leavedetails.html', {'all': x})

def leavereject(request,i):
    if request.method=='POST':
            x=Leavedetails.objects.get(id=i)
            x.status='Rejected'
            x.save()
            x=Leavedetails.objects.all()
            return redirect('leavedetails1')
            #return render(request,'leavedetails.html', {'all':x})
    else:
        x = Leavedetails.objects.all()
        return render(request, 'leavedetails.html', {'all': x})


def admindata(request):
    if request.method=='POST':
        #image=request.POST['image']
        name=request.POST['name']
        adminid=request.POST['adminid']
        jobtitle=request.POST['jobtitle']
        dept=request.POST['dept']
        location=request.POST['location']
        email=request.POST['email']
        phone=request.POST['phone']
        username=request.POST['username']
        password=request.POST['password']
        repassword=request.POST['repassword']
        print(name,adminid,dept,location,email,phone,username,password,repassword)

        admindataobj=Admindata()
        #admindataobj.image=request.POST['image']
        admindataobj.name=name
        admindataobj.adminid=adminid
        admindataobj.jobtitle=jobtitle
        admindataobj.dept=dept
        admindataobj.location=location
        admindataobj.email=email
        admindataobj.phone=phone
        admindataobj.username=username
        admindataobj.password=password
        admindataobj.repassword=repassword
        admindataobj.save()

        return redirect('addadmin')
