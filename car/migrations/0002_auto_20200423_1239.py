# Generated by Django 3.0.5 on 2020-04-23 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='customer_phone_number',
            field=models.PositiveIntegerField(),
        ),
    ]