# Generated by Django 3.0.3 on 2020-05-17 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200514_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextrainfo',
            name='bio',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userextrainfo',
            name='full_name',
            field=models.CharField(max_length=30),
        ),
    ]
