# Generated by Django 4.2.7 on 2024-09-30 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carte',
            name='filiere',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
