# Generated by Django 3.0.8 on 2020-07-02 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_boastsroasts_boolean'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boastsroasts',
            name='boast_or_roast',
            field=models.CharField(choices=[('Boast', 'Boast'), ('Roast', 'Roast')], default=None, max_length=5),
        ),
    ]