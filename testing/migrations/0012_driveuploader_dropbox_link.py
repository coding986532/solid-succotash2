# Generated by Django 4.0.2 on 2022-02-19 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0011_driveuploader_file_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='driveuploader',
            name='Dropbox_Link',
            field=models.CharField(blank=True, choices=[('dropbox.com', 'dropbox.com')], max_length=25),
        ),
    ]
