# Generated by Django 3.1.4 on 2020-12-28 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SpotidyToken',
            new_name='SpotifyToken',
        ),
    ]
