# Generated by Django 3.2.6 on 2021-09-16 20:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='Language_Pre',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='Mobile_Number',
            field=models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='Profile_Image',
            field=models.CharField(max_length=250),
        ),
    ]
