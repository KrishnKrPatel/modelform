from django.shortcuts import render
from .forms import ProductForm
from .models import Product
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'pages/index.html')

def input(request):
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            p=Product(pid=request.POST.get('pid'),
            pname=request.POST.get('pname'),
            pcost=request.POST.get('pcost'),
            pmfdt=request.POST.get('pmfdt'))

            p.save()
        return HttpResponse('Data inserted sucessfully...')
    else:
        form=ProductForm()
        return render(request,'pages/input.html',{'form':form})


def display(request):
    datas=Product.objects.all()

    return render(request,'pages/display.html',{'datas':datas})
