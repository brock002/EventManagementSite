# Generated by Django 3.0.3 on 2020-05-12 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200512_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextrainfo',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]
