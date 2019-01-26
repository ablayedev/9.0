# Generated by Django 2.1.3 on 2019-01-16 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lunette',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(max_length=250)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.CharField(max_length=250)),
                ('nature', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Lunette',
            },
        ),
    ]
