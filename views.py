from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Datas

def home(request):
    if request.method=='POST':
        name=request.POST['name']
        mail=request.POST['mail']
        contact=request.POST['contact']
        subject=request.POST['subject']
        message=request.POST['message']
        

        obj=Datas()
        obj.Name=name
        obj.Mail=mail
        obj.Contact=contact
        obj.Subject=subject
        obj.Message=message
        obj.save()
    return render(request,'home.html')
