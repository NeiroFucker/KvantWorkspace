# Generated by Django 3.1.5 on 2022-07-19 19:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('DiaryApp', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MailApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkUpdateNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DiaryApp.kvanthomework')),
            ],
            options={
                'db_table': 'workupdate_notifications',
            },
        ),
        migrations.CreateModel(
            name='WorkCreateNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DiaryApp.kvanthomework')),
            ],
            options={
                'db_table': 'workcreate_notifications',
            },
        ),
        migrations.CreateModel(
            name='TaskUpdateNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DiaryApp.kvanthometask')),
            ],
            options={
                'db_table': 'taskupdate_notifications',
            },
        ),
        migrations.CreateModel(
            name='TaskCreateNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DiaryApp.kvanthometask')),
            ],
            options={
                'db_table': 'taskcreate_notifications',
            },
        ),
        migrations.CreateModel(
            name='MailReceiveNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MailApp.kvantmessage')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'mail_notifications',
            },
        ),
        migrations.CreateModel(
            name='KvantNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('object_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'db_table': 'kvant_notifications',
            },
        ),
    ]
