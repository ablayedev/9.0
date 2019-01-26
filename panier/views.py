from django.shortcuts import render,get_object_or_404
from boutique.models import Lunette
from django.contrib.auth.models import User
from panier.models import Utilisateur
# Create your views here.


def index(request,id):
    panier_lunette=get_object_or_404(Lunette,id=id)
    context={
        'panier_lunette':panier_lunette
    }
    return render(request,'panier/detail_panier.html',context)

def register_sign(request):
    context={}
    if request.POST.get('register'):
        prenom=request.POST.get('prenom')
        nom=request.POST.get('nom')
        email_tel=request.POST.get('email_tel')
        user=User(first_name=prenom,username=nom)
        if prenom=="" or nom=="" or email_tel=="":
            context['erreur']="Veuillez completez tout les champs"
        else:
            user.save()
            utilisateur=Utilisateur(user=user,email_tel=email_tel)
            utilisateur.save()
            context['succes']="Félicitations,Inscription réussie"

        
    if request.POST.get('sign'):
        print('okkkk')
    
    return render(request,'panier/register_sign.html',context)