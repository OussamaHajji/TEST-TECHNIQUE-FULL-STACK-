# Generated by Django 4.1 on 2022-08-21 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_alter_venue_titre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='event_date',
            field=models.DateTimeField(null=True, verbose_name='event_date'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='titre',
            field=models.CharField(max_length=120, verbose_name='titre'),
        ),
    ]