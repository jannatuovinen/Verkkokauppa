# Generated by Django 5.0.4 on 2024-04-08 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kauppa', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tuote',
            options={'verbose_name': 'tuote', 'verbose_name_plural': 'tuotteet'},
        ),
        migrations.RenameField(
            model_name='tuote',
            old_name='teksti',
            new_name='nimi',
        ),
    ]