# Generated by Django 3.0.6 on 2020-06-05 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instamine', '0005_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, default='You can change this bio'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='image/hd5.jpeg', upload_to='image/'),
        ),
    ]