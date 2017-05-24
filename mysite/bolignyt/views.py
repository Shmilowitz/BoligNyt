from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import PythonBolig
# Create your views here.


# def index(request):
#     return render(request, 'bolignyt/home.html')


def index(request):
    python_bolig = PythonBolig.objects.order_by('-date_found')
    paginator = Paginator(python_bolig, 25) #vis 25 boliger
    side = request.GET.get('side')
    try:
        boliger = paginator.page(side)
    except PageNotAnInteger:
        boliger = paginator.page(1)

    except EmptyPage:
        boliger = paginator.page(paginator.num_pages)

    return render(request, 'bolignyt/header.html', {'boliger': boliger})

def contact(request):
    return render(request, 'bolignyt/basic.html',{'content':['Kontakt os her:','BoligNyt@gmail.com']})
