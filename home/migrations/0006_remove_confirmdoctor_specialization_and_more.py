# Generated by Django 4.0.3 on 2022-04-09 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_comments_field_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='confirmdoctor',
            name='Specialization',
        ),
        migrations.RemoveField(
            model_name='confirmdoctor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='confirmdoctor',
            name='gender',
        ),
    ]
