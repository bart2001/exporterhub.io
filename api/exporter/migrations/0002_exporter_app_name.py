# Generated by Django 3.1.3 on 2021-03-26 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exporter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exporter',
            name='app_name',
            field=models.CharField(max_length=45, null=True),
        ),
    ]
