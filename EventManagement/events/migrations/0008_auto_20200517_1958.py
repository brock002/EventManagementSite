# Generated by Django 3.0.3 on 2020-05-17 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_eventimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
