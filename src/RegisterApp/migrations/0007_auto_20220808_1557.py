# Generated by Django 3.1.5 on 2022-08-08 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegisterApp', '0006_auto_20220808_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffpersonalinfo',
            name='date',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='studydocument',
            name='year',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
