from django.shortcuts import render,get_object_or_404
from boutique.models import Lunette
# Create your views here.


def page_boutique(request):
    rayban=Lunette.objects.filter(marque="rayban")
    quartier=Lunette.objects.filter(marque="quartier")
    context={
        'active_menu':'active_menu',
        'rayban':rayban,
        'quartier':quartier,
        'lunette':Lunette.objects.all()
    }
    return render(request,'boutique/page_boutique.html',context)

def detail(request,id):
    detail_lunette=get_object_or_404(Lunette,id=id)
    context={
        'active_menu':'active_menu',
        'detail':detail_lunette
    }
    return render(request,'boutique/detail.html',context)