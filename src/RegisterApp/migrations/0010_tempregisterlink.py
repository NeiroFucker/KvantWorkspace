# Generated by Django 3.1.5 on 2022-08-10 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegisterApp', '0009_auto_20220810_1404'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempRegisterLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255)),
                ('permission', models.CharField(choices=[('Ученик', 'Ученик'), ('Учитель', 'Учитель'), ('Администратор', 'Администратор')], max_length=255)),
            ],
        ),
    ]
