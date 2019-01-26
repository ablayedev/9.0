from django.urls import path

app_name="panier"
from . import views
urlpatterns = [
    path('detail_panier/<int:id>',views.index,name="index"),
    path('register_sign/',views.register_sign,name="register_sign")
]
