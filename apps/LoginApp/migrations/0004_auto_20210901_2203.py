# Generated by Django 3.1.5 on 2021-09-01 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginApp', '0003_auto_20210823_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kvantuser',
            name='color',
            field=models.CharField(choices=[('green', 'green'), ('blue', 'blue'), ('pink', 'pink')], default='blue', max_length=100),
        ),
    ]