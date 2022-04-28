# Generated by Django 4.0.3 on 2022-04-28 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='Specialization',
            field=models.CharField(choices=[('Orthopedics', 'Orthopedics'), (' Internal Medicine', ' Internal Medicine'), ('Obstetrics and Gynecology', 'Obstetrics and Gynecology'), ('Dermatology', 'Dermatology'), ('Pediatrics', 'Pediatrics'), ('General Surgery', 'General Surgery'), ('Radiology', 'Radiology'), ('Ophthalmology', 'Ophthalmology'), (' Family Medicine', ' Family Medicine'), ('ENT', 'ENT')], max_length=500),
        ),
    ]
