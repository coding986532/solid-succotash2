# Generated by Django 3.2.11 on 2022-01-20 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0007_alter_visualstudiocodelink_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Excel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=250)),
                ('Date', models.DateTimeField()),
                ('Link', models.URLField(blank=True, max_length=1000)),
            ],
        ),
    ]
