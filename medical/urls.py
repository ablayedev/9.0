from django.urls import path 
app_name="medical"
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('maladie_oculaire/',views.maladie_occulaire,name="maladie_occulaire"),
    path('ophtalmologue/',views.ophtalmologue,name="opthalmologue")
]