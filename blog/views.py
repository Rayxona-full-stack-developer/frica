from django.shortcuts import render


# Create your views here.
def computers(request):
    return render(request,'computers.html',context={})

def contact(request):
    return render(request,'contact.html',context={})

def index(request):
    return render(request,'index.html',context={})

def mans_clothes(request):
    return render(request,'mans_clothes.html',context={})

def womans_clothes(request):
    return render(request,'womans_clothes.html',context={})