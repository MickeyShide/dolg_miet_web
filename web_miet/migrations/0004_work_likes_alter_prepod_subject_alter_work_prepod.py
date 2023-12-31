# Generated by Django 4.2.8 on 2023-12-14 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_miet', '0003_prepod_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='prepod',
            name='subject',
            field=models.ForeignKey(on_delete=models.SET('Удален'), to='web_miet.subject'),
        ),
        migrations.AlterField(
            model_name='work',
            name='prepod',
            field=models.ForeignKey(on_delete=models.SET('Удален'), to='web_miet.prepod'),
        ),
    ]
