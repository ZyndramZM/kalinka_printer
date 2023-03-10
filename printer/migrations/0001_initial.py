# Generated by Django 4.1.5 on 2023-01-28 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pathlib


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_org', models.FileField(upload_to=pathlib.PureWindowsPath('Q:/Dokumenty/!Studia/!Projects/kalinka_printer/printer/uploads/org'))),
                ('file_pdf', models.FileField(null=True, upload_to=pathlib.PureWindowsPath('Q:/Dokumenty/!Studia/!Projects/kalinka_printer/printer/uploads/pdf'))),
                ('mono', models.BooleanField(null=True)),
                ('pages', models.IntegerField(null=True)),
                ('orientation', models.CharField(choices=[('P', 'Pionowa'), ('L', 'Pozioma')], default='P', max_length=1, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PrintJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(null=True)),
                ('status', models.CharField(choices=[('ST', 'Nadany'), ('PD', 'Oczekuje'), ('IN', 'W trakcie drukowania'), ('OK', 'Ukończono'), ('FD', 'Błąd')], default='ST', max_length=2)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='printer.document')),
            ],
        ),
    ]
