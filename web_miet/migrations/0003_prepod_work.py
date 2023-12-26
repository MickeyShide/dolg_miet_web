# Generated by Django 4.2.8 on 2023-12-14 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_miet', '0002_subject_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prepod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='web_miet.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=250)),
                ('prepod', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='web_miet.prepod')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='web_miet.subject')),
            ],
        ),
    ]