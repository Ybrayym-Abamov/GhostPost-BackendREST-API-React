# Generated by Django 3.0.8 on 2020-07-02 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_boastsroasts_boast_or_roast'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boastsroasts',
            name='boolean',
        ),
    ]