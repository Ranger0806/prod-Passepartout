# Generated by Django 5.1.3 on 2024-11-09 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_projectuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectuser',
            name='countries',
            field=models.IntegerField(default=0),
        ),
    ]
