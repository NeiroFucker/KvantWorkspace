# Generated by Django 3.1.5 on 2022-08-08 07:26

import RegisterApp.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('RegisterApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livingadress',
            name='city',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='livingadress',
            name='house_number',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='livingadress',
            name='room',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='livingadress',
            name='street',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='personalitydocument',
            name='code',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='personalitydocument',
            name='given_date',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='personalitydocument',
            name='number',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='personalitydocument',
            name='series',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='personalitydocument',
            name='who_gave',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='staffpersonalinfo',
            name='adress',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='RegisterApp.livingadress'),
        ),
        migrations.AlterField(
            model_name='staffpersonalinfo',
            name='date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='staffpersonalinfo',
            name='document',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='RegisterApp.personalitydocument'),
        ),
        migrations.AlterField(
            model_name='staffpersonalinfo',
            name='sex',
            field=models.CharField(blank=True, choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], max_length=255),
        ),
        migrations.AlterField(
            model_name='staffpersonalinfo',
            name='snils',
            field=models.CharField(blank=True, max_length=255, validators=[RegisterApp.validators.validate_telephone]),
        ),
        migrations.AlterField(
            model_name='staffpersonalinfo',
            name='study',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='RegisterApp.studydocument'),
        ),
        migrations.AlterField(
            model_name='staffpersonalinfo',
            name='telephone',
            field=models.CharField(blank=True, max_length=255, validators=[RegisterApp.validators.validate_telephone]),
        ),
        migrations.AlterField(
            model_name='staffpersonalinfo',
            name='user',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='studentparent',
            name='adress',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='RegisterApp.livingadress'),
        ),
        migrations.AlterField(
            model_name='studentparent',
            name='date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='studentparent',
            name='document',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='RegisterApp.personalitydocument'),
        ),
        migrations.AlterField(
            model_name='studentparent',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='studentparent',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='studentparent',
            name='surname',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='studentparent',
            name='telephone',
            field=models.CharField(blank=True, max_length=255, validators=[RegisterApp.validators.validate_telephone]),
        ),
        migrations.AlterField(
            model_name='studentparent',
            name='work_place',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='studentparent',
            name='work_title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='studentpersonalinfo',
            name='adress',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='RegisterApp.livingadress'),
        ),
        migrations.AlterField(
            model_name='studentpersonalinfo',
            name='date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='studentpersonalinfo',
            name='document',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='RegisterApp.personalitydocument'),
        ),
        migrations.AlterField(
            model_name='studentpersonalinfo',
            name='father',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='father', to='RegisterApp.studentparent'),
        ),
        migrations.AlterField(
            model_name='studentpersonalinfo',
            name='is_dzd',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Нет', 'Нет')], max_length=255),
        ),
        migrations.AlterField(
            model_name='studentpersonalinfo',
            name='mother',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mother', to='RegisterApp.studentparent'),
        ),
        migrations.AlterField(
            model_name='studentpersonalinfo',
            name='school',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='studentpersonalinfo',
            name='school_class',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='studentpersonalinfo',
            name='sex',
            field=models.CharField(blank=True, choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], max_length=255),
        ),
        migrations.AlterField(
            model_name='studentpersonalinfo',
            name='snils',
            field=models.CharField(blank=True, max_length=255, validators=[RegisterApp.validators.validate_telephone]),
        ),
        migrations.AlterField(
            model_name='studentpersonalinfo',
            name='telephone',
            field=models.CharField(blank=True, max_length=255, validators=[RegisterApp.validators.validate_telephone]),
        ),
        migrations.AlterField(
            model_name='studydocument',
            name='qualification',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='studydocument',
            name='speciality',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='studydocument',
            name='vpo_spo',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='studydocument',
            name='vuz',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='studydocument',
            name='year',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
