# Generated by Django 3.1.5 on 2022-08-07 18:28

import RegisterApp.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LivingAdress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('house_number', models.CharField(max_length=255)),
                ('room', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalityDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=255)),
                ('given_date', models.CharField(max_length=255)),
                ('who_gave', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StudentParent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('work_place', models.CharField(max_length=255)),
                ('work_title', models.CharField(max_length=255)),
                ('patronymic', models.CharField(blank=True, max_length=255)),
                ('telephone', models.CharField(max_length=255, validators=[RegisterApp.validators.validate_telephone])),
                ('adress', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='RegisterApp.livingadress')),
                ('document', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='RegisterApp.personalitydocument')),
            ],
        ),
        migrations.CreateModel(
            name='StudyDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField()),
                ('vpo_spo', models.CharField(max_length=255)),
                ('vuz', models.CharField(max_length=255)),
                ('speciality', models.CharField(max_length=255)),
                ('qualification', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StudentPersonalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('school_class', models.PositiveIntegerField()),
                ('school', models.CharField(max_length=255)),
                ('sex', models.CharField(choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], max_length=255)),
                ('is_dzd', models.CharField(choices=[('Да', 'Да'), ('Нет', 'Нет')], max_length=255)),
                ('snils', models.CharField(max_length=255, validators=[RegisterApp.validators.validate_telephone])),
                ('telephone', models.CharField(max_length=255, validators=[RegisterApp.validators.validate_telephone])),
                ('adress', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='RegisterApp.livingadress')),
                ('document', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='RegisterApp.personalitydocument')),
                ('father', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='father', to='RegisterApp.studentparent')),
                ('mother', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mother', to='RegisterApp.studentparent')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StaffPersonalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('sex', models.CharField(choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], max_length=255)),
                ('snils', models.CharField(max_length=255, validators=[RegisterApp.validators.validate_telephone])),
                ('telephone', models.CharField(max_length=255, validators=[RegisterApp.validators.validate_telephone])),
                ('adress', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='RegisterApp.livingadress')),
                ('document', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='RegisterApp.personalitydocument')),
                ('study', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='RegisterApp.studydocument')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]