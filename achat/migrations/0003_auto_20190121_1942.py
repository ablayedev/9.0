# Generated by Django 2.1.3 on 2019-01-21 18:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('achat', '0002_remove_achat_prenom'),
    ]

    operations = [
        migrations.AddField(
            model_name='achat',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='achat',
            name='prix',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=50),
        ),
    ]
