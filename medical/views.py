from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'medical/index.html')

def maladie_occulaire(request):
    return render(request,'medical/maladie_occulaire.html')

def ophtalmologue(request):
    return render(request,'medical/ophtalmologue.html')