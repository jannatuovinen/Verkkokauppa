# Generated by Django 5.0.4 on 2024-04-08 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tuote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teksti', models.CharField(max_length=200)),
                ('hinta', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
    ]
