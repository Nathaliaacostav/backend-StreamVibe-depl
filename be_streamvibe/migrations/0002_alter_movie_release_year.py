# Generated by Django 5.0.4 on 2024-05-30 00:54

import be_streamvibe.models.movie
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('be_streamvibe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_year',
            field=models.IntegerField(default=be_streamvibe.models.movie.get_current_year),
        ),
    ]
