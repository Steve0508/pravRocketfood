# Generated by Django 5.0.8 on 2024-08-11 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datas',
            old_name='Address',
            new_name='Message',
        ),
        migrations.RemoveField(
            model_name='datas',
            name='Age',
        ),
        migrations.AddField(
            model_name='datas',
            name='Subject',
            field=models.CharField(default='', max_length=50),
        ),
    ]
