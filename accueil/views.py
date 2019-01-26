from django.shortcuts import render
from boutique.models import Lunette,Satisfait
# Create your views here.


def index(request):
    context={
        'active_menu':'active_menu',
        'lunette':Lunette.objects.filter(nature="mode"),
        'soleil':Lunette.objects.filter(nature="soleil"),
        'vue':Lunette.objects.filter(nature="vue"),
        'satisfait':Satisfait.objects.all()
    }
    
    return render(request,'accueil/index.html',context)

def shooting(request):
    return render(request,'accueil/shooting.html')