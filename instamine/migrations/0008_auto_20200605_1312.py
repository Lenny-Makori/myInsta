# Generated by Django 3.0.6 on 2020-06-05 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instamine', '0007_auto_20200605_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='image/download.png', upload_to='image/'),
        ),
    ]
