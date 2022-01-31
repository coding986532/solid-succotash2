# Generated by Django 3.2.11 on 2022-01-31 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0019_alter_assignment_resolved'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Time', models.DateTimeField()),
                ('To', models.CharField(choices=[('test', 'test'), ('C,H', 'C,H'), ('S,A', 'S,A'), ('S,L', 'S,L')], max_length=250)),
                ('Subject', models.CharField(blank=True, max_length=250)),
                ('Message', models.CharField(max_length=250)),
                ('From', models.CharField(choices=[('test', 'test'), ('C,H', 'C,H'), ('S,A', 'S,A'), ('S,L', 'S,L')], max_length=250)),
            ],
        ),
    ]