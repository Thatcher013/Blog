# Generated by Django 2.1.5 on 2019-08-09 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_picture',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Profil Fotoğrafı'),
        ),
    ]