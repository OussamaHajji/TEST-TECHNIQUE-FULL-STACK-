# Generated by Django 4.1 on 2022-08-21 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_alter_venue_event_date_alter_venue_titre'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='latitude',
            field=models.DecimalField(decimal_places=3, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='longitude',
            field=models.DecimalField(decimal_places=3, max_digits=8, null=True),
        ),
    ]
