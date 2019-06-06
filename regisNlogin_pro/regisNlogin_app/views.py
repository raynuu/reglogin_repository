from django.shortcuts import render
from django.http.response import HttpResponse
from .models import registration,login
from .forms import registrationform,loginform

# Create your views here.
def home_view(request):
    if request.method=='POST':
        iform=registrationform(request.POST)
        if iform.is_valid():
            iform.save()
            iform=registrationform()
            return render(request,'registration.html',{'rform':iform})
        else:
            return HttpResponse('invalid data')
    else:
        iform=registrationform()
        return render(request,'registration.html',{'rform':iform})

def login_view(request):
    if request.method=='POST':
        lform=loginform(request.POST)
        if lform.is_valid():
            lform.save()
            lform=loginform()
            return render(request,'login.html',{'lform':lform})
        else:
            return HttpResponse('INVALID DATA')
    else:
        lform=loginform()
        return render(request,'login.html',{'lform':lform})






















