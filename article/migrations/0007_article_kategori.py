# Generated by Django 2.1.5 on 2019-07-30 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20190730_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='kategori',
            field=models.TextField(choices=[('Yazılım', 'Yazılım'), ('Şiir', 'Şiir'), ('Fikir', 'Fikir')], default='Yok', verbose_name='Kategori'),
        ),
    ]