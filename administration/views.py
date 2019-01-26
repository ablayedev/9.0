from django.shortcuts import render,get_object_or_404,redirect
from administration.forms import MembreForm
from django.contrib.auth import authenticate, login,logout
from achat.models import Achat
from django.utils import timezone
# Create your views here.

def MembreView(request):
    error=""
    if request.method=="POST":
        forms=MembreForm(request.POST)
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        print(user)
        if user is not None:
            login(request,user)
            return redirect('administration:reception')
        else:
           error="Veuillez saisir correctement les identifiants"      
    else:
        forms=MembreForm()
    context={
        'forms':forms,
        'error':error
    }
    return render(request,'administration/index.html',context)

def reception(request):
    achat=Achat.objects.all()
    context={
        'achat':achat
    }
    return render(request,'administration/reception.html',context)

def detail(request,id):
    achat=get_object_or_404(Achat,id=id)
    context={
        'achat':achat,
        'date':timezone.now()
    }
    return render(request,'administration/detail.html',context)

def deconect(request):
    logout(request)
    return redirect('administration:sign')

def supprimer(request,id):
    sup=get_object_or_404(Achat,id=id)
    sup.delete()
    return redirect('administration:reception')