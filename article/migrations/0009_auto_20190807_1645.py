# Generated by Django 2.1.5 on 2019-08-07 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_article_view'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='view',
            field=models.IntegerField(verbose_name='Görüntülenme'),
        ),
    ]