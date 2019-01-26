from django.urls import path
from . import views

app_name="boutique"
urlpatterns = [
    path('',views.page_boutique,name="page_boutique"),
    path('detail/<int:id>',views.detail,name="detail")
]
