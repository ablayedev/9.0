from django.db import models
from django.utils import timezone
# Create your models here.

class Achat(models.Model):
    tel=models.CharField(max_length=250)
    nom=models.CharField(max_length=250)
    adresse=models.CharField(max_length=250)
    livraison=models.CharField(max_length=250)
    lunette=models.ImageField(upload_to="photos/achat")
    date=models.DateTimeField(default=timezone.now)
    prix=models.DecimalField(max_digits=50,decimal_places=2,default=00000.00)
    def __str__(self):
        return self.tel

