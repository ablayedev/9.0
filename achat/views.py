from django.shortcuts import render,get_object_or_404
from boutique.models import Lunette
from achat.models import Achat
# Create your views here.
def index(request,id):
    context={}
    achat_lunette=get_object_or_404(Lunette,id=id)
    if request.method=="POST":
        nom_complet=request.POST.get('nom')
        adresse=request.POST.get('adresse')
        tel=request.POST.get('tel')
        livraison=request.POST.get('group1')
        lunette=achat_lunette.image
        prix=achat_lunette.prix
        if nom_complet=="" or adresse=="" or tel=="" or livraison=="":
            context['error']="veuillez completez tout les champs"
        else:
            achat=Achat()
            achat.nom=nom_complet
            achat.adresse=adresse
            achat.tel=tel
            achat.livraison=livraison
            achat.lunette=lunette
            achat.prix=prix
            achat.save()
            context['succes']="Votre commande a bien été enregistré"
    
    context['achat_lunette']=achat_lunette
    
    return render(request,'achat/index.html',context)