# Generated by Django 3.0.8 on 2020-07-02 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boastsroasts',
            name='score',
        ),
    ]
