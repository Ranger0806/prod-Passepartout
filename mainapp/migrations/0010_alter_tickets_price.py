# Generated by Django 5.1.3 on 2024-11-10 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_alter_tickets_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]