# Generated by Django 4.0.4 on 2022-05-14 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bolim1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='muallif',
            name='kitob_soni',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]