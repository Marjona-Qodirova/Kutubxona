# Generated by Django 4.0.4 on 2022-05-17 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bolim1', '0002_muallif_kitob_soni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='muallif',
            name='tirik',
            field=models.BooleanField(blank=True),
        ),
    ]
