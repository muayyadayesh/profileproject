# Generated by Django 3.2.6 on 2021-09-16 16:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Language_Pre', models.CharField(choices=[('EN', 'EN'), ('DE', 'DE')], max_length=10)),
                ('Reading', models.CharField(max_length=10)),
                ('Writing', models.CharField(max_length=10)),
                ('Speaking', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Profile_Image', models.ImageField(blank=True, upload_to='uploaded_pics/')),
                ('First_name', models.CharField(max_length=250)),
                ('Father_name', models.CharField(max_length=250)),
                ('Middle_name', models.CharField(max_length=250)),
                ('Last_name', models.CharField(max_length=250)),
                ('Full_address', models.CharField(max_length=300)),
                ('Birthdate', models.DateField()),
                ('Bio', models.CharField(max_length=300)),
                ('Gender', models.IntegerField(choices=[(0, 'male'), (1, 'female'), (2, 'not specified')])),
                ('Country_Birth', models.CharField(max_length=250)),
                ('Country_Residence', models.CharField(max_length=250)),
                ('Linkedin_URL', models.URLField()),
                ('Mobile_Number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
            ],
        ),
    ]