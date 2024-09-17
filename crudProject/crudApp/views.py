from django.shortcuts import render, redirect
from.models import Student
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string
from datetime import datetime


date=datetime.now()

# Create your views here.
def home(request):
    # data=Student.objects.all()# query set or model instance
    data=Student.objects.filter(ISDelete=False)  # to remove deleted data from frontend
    
    return render(request,"crudApp/home.html", {'data': data })

def form(request):
    if(request.method=="POST"):
        data=request.POST
        nm=data['name']
        age=data['age']
        emil=data["email"]
        msg=data['message']
        
        Student.objects.create(name=nm, age=age, email=emil,message=msg)
        subject='python with django trainging'
        # message="thanks for filling our form"
        message=render_to_string('crudApp/msg.html',{'name':nm,'date':date})
        from_email='rajendra2057.02.04@gmail.com'
        recipient_list=[emil,'rajendra2057rawal@gmail.com']
        # send_mail(subject,message,from_email,recipient_list,fail_silently=False)
                # to send staticfiles
        email_msg=EmailMessage(subject,message,from_email,recipient_list)
        email_msg.attach_file("Cv.pdf")
        email_msg.send(fail_silently=True)
        
        
        messages.success(request,f"hi {nm} your form is successfully submitted please check your mail")
        return redirect("form")
        # return HttpResponse ("successfully submitted")
    return render(request,"crudApp/form.html")

def contact(request):
    return render(request,"crudApp/contact.html")

def about(request):
    return render(request,"crudApp/about.html")

def delete_data(request,id):
    data=Student.objects.get(id=id)
    data.ISDelete=True
    data.save()
    messages.success(request,"successfully deleted")
    return redirect("home")


def edit(request,id):
    
    data=Student.objects.get(id=id)
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        email=request.POST['email']
        message=request.POST['message']
        
        data.name=name
        data.age=age
        data.email=email
        data.message=message
        
        data.save()
        return redirect('home')
        
    return render(request,'crudApp/edit.html',{'data':data})

from django.db.models import Q  #query set
 
def search(request):

    if request.method=='GET':
        searched=request.GET['searched']
        finds=Student.objects.filter(Q(name__icontains=searched)|Q(age__icontains=searched) )
        finds=finds.filter(ISDelete=False)
        
    return render(request,'crudApp/search.html',{'finds':finds})

def bin(request):
    finds=Student.objects.filter(ISDelete=True)
    
    return render(request,'crudApp/bin.html',{'finds':finds})
    
    
def restore(request,id):
    data=Student.objects.get(id=id)
    data.ISDelete=False
    data.save()
    return redirect('home')


def delete_bin(request,id):
    data=Student.objects.get(id=id)
    data.delete()
    
    return redirect('bin')




#_______________________________________________
#_______________________________________________
#authentication part

def log_in(request):
    return render(request, 'auth/login.html')

def register(request):
    return render(request, 'auth/register.html')

