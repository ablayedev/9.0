from django.db import models

# Create your models here.


#LUNETTES DE SOLEIL

nature_lunette=(
    ('soleil','soleil'),
    ('vue','vue'),
    ('mode','mode'),
    ('classe','classe'),

)
marque_lunette=(
    ('rayban','rayban'),
    ('quartier','quartier'),
)
class Lunette(models.Model):
    
    marque=models.CharField(max_length=250,choices=marque_lunette)
    prix=models.DecimalField(max_digits=50,decimal_places=2)
    description=models.CharField(max_length=250)
    nature=models.CharField(max_length=250,choices=nature_lunette)
    image=models.ImageField(upload_to='photos/',default="a.jpg")

    class Meta:
        verbose_name ="Lunette"
        

    def __str__(self):
        return self.nature

class Satisfait(models.Model):
    image=models.ImageField(upload_to='photos/satisfaits',default="a.jpg")

    class Meta:
        verbose_name ="Satisfait"
        

   


   
