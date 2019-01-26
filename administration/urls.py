from django.urls import path
from administration import views
app_name='administration'
urlpatterns = [
    path('sign/',views.MembreView,name="sign"),
    path('reception/',views.reception,name="reception"),
    path('detail/<int:id>/',views.detail,name="detail"),
    path('deconect/',views.deconect,name="deconect"),
    path('supprimer/<int:id>/',views.supprimer,name="supprimer")
]
