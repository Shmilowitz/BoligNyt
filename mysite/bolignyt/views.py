from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import PythonBolig
# Create your views here.


def index(request):
    return render(request, 'bolignyt/home.html')


def contact(request):
    return render(request, 'bolignyt/basic.html',{'content':['Kontakt os her:','BoligNyt@gmail.com']})
