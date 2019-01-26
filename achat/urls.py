from django.urls import path

app_name="achat"
from . import views
urlpatterns = [
    path('achat/<int:id>',views.index,name="index")
]
