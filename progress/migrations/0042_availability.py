# Generated by Django 3.2.12 on 2022-02-17 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0041_alter_messages_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(choices=[('test', 'test'), ('C,H', 'C,H'), ('S,A', 'S,A'), ('S,L', 'S,L')], max_length=5)),
                ('Available', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5)),
                ('On_Docs', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5)),
            ],
        ),
    ]
