# Generated by Django 3.1.5 on 2022-08-08 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegisterApp', '0002_auto_20220808_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentparent',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentpersonalinfo',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
