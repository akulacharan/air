from django.shortcuts import render
from . models import Destination

# Create your views here.
def index(request):
    dests=Destination.objects.all()
    return render(request,'index.html',{'dests':dests})

def place(request):
    dests = Destination.objects.all()
    return render(request,'destinations.html',{'dests':dests})

def news(request):
    return render(request,'news.html')

def home(request):
    dests = Destination.objects.all()
    return render(request,'index.html',{'dests':dests})

def con(request):
    return render(request,'contact.html')

