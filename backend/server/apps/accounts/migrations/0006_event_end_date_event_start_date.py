# Generated by Django 4.2.7 on 2023-11-07 18:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_seat_event_event_category_delete_eventimage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='end_date',
            field=models.DateField(default=datetime.date(2023, 11, 22)),
        ),
        migrations.AddField(
            model_name='event',
            name='start_date',
            field=models.DateField(default=datetime.date(2023, 11, 7)),
        ),
    ]
