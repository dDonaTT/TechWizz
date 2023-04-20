# Generated by Django 3.0.7 on 2023-04-16 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produktet', '0003_auto_20230415_2359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='lloji_i_panelit',
        ),
        migrations.AddField(
            model_name='product',
            name='lloji_panelit',
            field=models.CharField(blank=True, choices=[('IPS', 'IPS'), ('VA', 'VA'), ('TN', 'TN')], max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='lloji',
            field=models.CharField(choices=[('laptop', 'Laptop'), ('monitor', 'Monitor'), ('kompjuter', 'Kompjuter')], default='laptop', max_length=10),
        ),
    ]