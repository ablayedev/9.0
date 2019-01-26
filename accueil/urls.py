from django.urls import path

app_name="accueil"
from . import views
urlpatterns = [
    path('',views.index,name="index"),
   
]
